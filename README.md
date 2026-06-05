# 💀 DHCP Starvation Attack — Seguridad de Redes

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scapy](https://img.shields.io/badge/Scapy-Latest-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux-orange?style=for-the-badge&logo=linux)
![License](https://img.shields.io/badge/Uso-Educativo-red?style=for-the-badge)

**Sael Germán García** | Matrícula: `2025-0725`  
Asignatura: Seguridad de Redes | Profesor: Jonathan Rondón  
Instituto Tecnológico de las Américas — ITLA | 2026

</div>

---

## 📋 Descripción del Ataque

El **DHCP Starvation Attack** (también conocido como DHCP Exhaustion) explota la ausencia de autenticación en el protocolo **DHCP**. Mediante la simulación masiva de clientes falsos con direcciones MAC aleatorizadas (**MAC Spoofing**), se consume la totalidad del pool de direcciones IP del servidor legítimo (R1), generando una **Denegación de Servicio (DoS)** que impide a los usuarios reales obtener conectividad de red.

> 💡 **Prerrequisito:** El nodo atacante opera sobre un enlace **Trunk 802.1Q** en e0/3 de SW1, permitiéndole inyectar peticiones DHCP Discover falsificadas en múltiples VLANs simultáneamente.

---

## 🗺️ Topología de Red

### 📊 Segmentación de VLANs

| VLAN ID | Nombre | Segmento IP | Descripción |
|:-------:|:------:|:-----------:|-------------|
| 10 | Usuarios | 10.7.25.0/24 | VPC1 — Pool objetivo del agotamiento |
| 20 | Servidores | 10.7.20.0/24 | VPC2 — Pool objetivo del agotamiento |
| Trunk | Inter-VLAN | Múltiple | e0/3 de SW1 en modo Trunk dot1q para el atacante |

### 📊 Matriz de Direccionamiento

| Elemento | Dirección IP | Interfaz | Estado |
|:--------:|:------------:|:--------:|--------|
| Servidor DHCP (R1) | 10.7.25.1 / 10.7.20.1 | Eth0/0.10 y .20 | Activo — Vulnerable al agotamiento |
| Atacante | Múltiple | ens4.10, ens4.20 | Enviando ráfagas masivas de DHCP Discover |
| Víctima (VPC1/VPC2) | Dinámica | Eth0 | Incapaz de obtener IP (`Can't find dhcp server`) |

---

## ⚙️ Requisitos

```bash
# Sistema Operativo
Ubuntu Linux (recomendado)

# Dependencias
sudo apt update && sudo apt install -y python3-scapy python3-pip

# Privilegios requeridos
sudo / root
```

---

## 🔧 Configuración Previa

### Habilitar Trunk en SW1
```cisco
SW1(config)# interface ethernet0/3
SW1(config-if)# switchport trunk encapsulation dot1q
SW1(config-if)# switchport mode trunk
SW1(config-if)# no shutdown
SW1(config-if)# end
SW1# write memory
```

### Crear subinterfaces 802.1Q en el atacante
```bash
sudo ip link add link ens4 name ens4.10 type vlan id 10
sudo ip link add link ens4 name ens4.20 type vlan id 20
sudo ip link set ens4.10 up
sudo ip link set ens4.20 up
```

---

## 🚀 Uso

```bash
# Ejecutar el ataque (por defecto: 200 paquetes por interfaz)
sudo python3 dhcp_starvation.py

# Especificar cantidad de paquetes
sudo python3 dhcp_starvation.py 2000

# Verificar el colapso del Pool en R1
R1# show ip dhcp pool
R1# show ip dhcp binding

# Verificar DoS en la víctima
VPCS> ip dhcp
# Resultado esperado: DDD Can't find dhcp server
```

---

## 🔬 ¿Cómo funciona?

| Paso | Función | Descripción |
|:----:|:-------:|-------------|
| 1️⃣ | `INTERFACES` | Define las subinterfaces `ens4.10` y `ens4.20` como vectores de ataque |
| 2️⃣ | `random_mac()` | Genera MACs Unicast completamente aleatorias (máscara `& 0xFC` en el primer octeto) |
| 3️⃣ | `mac_to_bytes()` | Convierte la MAC a bytes para poblar correctamente el campo `chaddr` de BOOTP |
| 4️⃣ | `flood_iface()` | Construye y despacha paquetes DHCP Discover con `sendp()` en bucle por cada VLAN |
| 5️⃣ | `dhcp_starvation()` | Lanza hilos paralelos con `threading` para atacar ambas VLANs a la vez, agotando los pools en segundos |

### Estructura del Paquete Malicioso

| Capa | Campo | Valor |
|:----:|:-----:|-------|
| L2 Ethernet | `src` / `dst` | MAC falsa / `ff:ff:ff:ff:ff:ff` (Broadcast) |
| L3 IP | `src` / `dst` | `0.0.0.0` / `255.255.255.255` (Broadcast) |
| L4 UDP | `sport` / `dport` | `68` (cliente) / `67` (servidor) |
| L7 BOOTP/DHCP | `chaddr` / `xid` | MAC falsa en bytes / Transaction ID aleatorio |

---

## 🛡️ Contramedidas

### 1. Habilitar Port Security en SW1
```cisco
SW1(config)# interface ethernet0/3
SW1(config-if)# switchport port-security
SW1(config-if)# switchport port-security maximum 2
SW1(config-if)# switchport port-security violation restrict
SW1(config-if)# exit
```

### 2. Limitar tasa de peticiones DHCP (DHCP Snooping)
```cisco
SW1(config-if)# ip dhcp snooping limit rate 10
```

### 3. Flujo de diagnóstico completo
```bash
# 1. Limpiar lease previo en la víctima
VPCS> clear ip

# 2. Ejecutar el ataque
Ubuntu$ sudo python3 dhcp_starvation.py 2000

# 3. Verificar colapso del Pool
R1# show ip dhcp pool

# 4. Limpiar tablas lógicas del Gateway
R1# clear ip dhcp binding *

# 5. Verificar DoS exitoso en el cliente
VPCS> ip dhcp
```

---

## 📁 Archivos del Repositorio

| Archivo | Descripción |
|:-------:|-------------|
| [`dhcp_starvation.py`](dhcp_starvation.py) | Script principal del ataque |
| [`SaelGermanGarcia_2025-0725_DHCP_Starvation_P1.pdf`](SaelGermanGarcia_2025-0725_DHCP_Starvation_P1.pdf) | Documentación técnica completa |

---

## 🖼️ Capturas de Pantalla

- 📸 [Ejecución y Despliegue Masivo del Ataque DHCP Starvation](Capturas%20de%20Pantalla%20DHCP%20Starvation/Ejecuci%C3%B3n%20y%20Despliegue%20Masivo%20del%20Ataque%20DHCP%20Starvation.png)
- 📸 [Ejecución y Despliegue Masivo](Capturas%20de%20Pantalla%20DHCP%20Starvation/Ejecuci%C3%B3n%20y%20Despliegue%20Masivo.png)
- 📸 [Agotamiento Total de los Pools DHCP en el Gateway](Capturas%20de%20Pantalla%20DHCP%20Starvation/Agotamiento%20Total%20de%20los%20Pools%20DHCP%20en%20el%20Gateway2.png)
- 📸 [Saturación de la Tabla de Asignaciones Lógicas (DHCP Bindings)](Capturas%20de%20Pantalla%20DHCP%20Starvation/Saturaci%C3%B3n%20de%20la%20Tabla%20de%20Asignaciones%20L%C3%B3gicas%20(DHCP%20Bindings).png)
- 📸 [Saturación de la Tabla de Asignaciones Lógicas (DHCP Bindings) 2](Capturas%20de%20Pantalla%20DHCP%20Starvation/Saturaci%C3%B3n%20de%20la%20Tabla%20de%20Asignaciones%20L%C3%B3gicas%20(DHCP%20Bindings)2.png)
- 📸 [Denegación de Servicio (DoS) Efectiva en el Cliente Víctima](Capturas%20de%20Pantalla%20DHCP%20Starvation/Denegaci%C3%B3n%20de%20Servicio%20(DoS)%20Efectiva%20en%20el%20Cliente%20V%C3%ADctima.png)
- 📸 [Contramedida Aplicada](Capturas%20de%20Pantalla%20DHCP%20Starvation/contramedidass.png)

---

## 📎 Recursos

📄 **Documentación Técnica:** [Ver Informe PDF](SaelGermanGarcia_2025-0725_DHCP_Starvation_P1.pdf)  
▶️ **Video Demostración:** [Ver en YouTube](https://youtube.com/playlist?list=PLV_dKVnYXf6dpmk3j8uXPHAZdbrkCQGAY)

---

## 📚 Referencias

1. Cisco Systems. *Port Security Configuration Guide*. Documentación oficial de Cisco IOS.
2. Scapy Project. *Scapy: Interactive packet manipulation program*. [https://scapy.net/](https://scapy.net/)
3. IETF. *RFC 2131: Dynamic Host Configuration Protocol*. Especificación base del protocolo DHCP.
4. Reconocimiento especial: Troubleshooting, base del script y documentación apoyado en Inteligencia Artificial.

---

<div align="center">

⚠️ **AVISO LEGAL** ⚠️  
*Este script fue desarrollado exclusivamente con fines académicos y educativos.*  
*Su uso en redes sin autorización explícita es ilegal y éticamente inaceptable.*

</div>
