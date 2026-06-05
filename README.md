[dhcp_starvation_readme_v2.html](https://github.com/user-attachments/files/28645810/dhcp_starvation_readme_v2.html)

<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --gh-bg: #0d1117; --gh-surface: #161b22; --gh-border: #30363d;
  --gh-text: #e6edf3; --gh-muted: #8b949e; --gh-accent: #58a6ff;
  --gh-green: #3fb950; --gh-orange: #f0883e; --gh-red: #f85149;
  --gh-purple: #bc8cff; --gh-yellow: #e3b341;
}
.wrap { background: var(--gh-bg); color: var(--gh-text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6; padding: 24px; border-radius: 8px; border: 1px solid var(--gh-border); }
.repo-header { display: flex; align-items: center; gap: 8px; color: var(--gh-accent); font-size: 20px; font-weight: 600; margin-bottom: 6px; }
.repo-header i { font-size: 22px; color: var(--gh-muted); }
.repo-desc { color: var(--gh-muted); font-size: 13px; margin-bottom: 16px; }
.badges { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
.badge { display: inline-flex; align-items: center; border-radius: 4px; font-size: 11px; font-weight: 600; overflow: hidden; font-family: monospace; }
.badge-label { background: #555; color: #fff; padding: 3px 8px; }
.badge-value { padding: 3px 8px; color: #fff; }
.b-blue { background: #007ec6; } .b-green { background: #4c1; } .b-orange { background: #e05d44; } .b-gray { background: #555; } .b-red { background: #c0392b; } .b-purple { background: #8e44ad; }
hr { border: none; border-top: 1px solid var(--gh-border); margin: 18px 0; }
h2 { font-size: 17px; font-weight: 600; color: var(--gh-text); margin: 18px 0 10px; border-bottom: 1px solid var(--gh-border); padding-bottom: 6px; }
h3 { font-size: 14px; font-weight: 600; color: var(--gh-accent); margin: 14px 0 6px; }
p { margin-bottom: 10px; color: var(--gh-text); }
.muted { color: var(--gh-muted); } .accent { color: var(--gh-accent); } .green { color: var(--gh-green); } .orange { color: var(--gh-orange); } .red { color: var(--gh-red); } .yellow { color: var(--gh-yellow); }
code { font-family: 'SFMono-Regular', Consolas, monospace; font-size: 12px; background: #161b22; border: 1px solid var(--gh-border); border-radius: 4px; padding: 1px 5px; color: var(--gh-orange); }
pre { background: var(--gh-surface); border: 1px solid var(--gh-border); border-radius: 6px; padding: 14px 16px; overflow-x: auto; margin: 10px 0; font-size: 12px; line-height: 1.5; font-family: 'SFMono-Regular', Consolas, monospace; }
.code-header { background: #21262d; border: 1px solid var(--gh-border); border-bottom: none; border-radius: 6px 6px 0 0; padding: 6px 14px; font-size: 12px; color: var(--gh-muted); display: flex; align-items: center; gap: 6px; }
.code-header + pre { border-radius: 0 0 6px 6px; margin-top: 0; }
table { width: 100%; border-collapse: collapse; font-size: 13px; margin: 10px 0; }
th { background: var(--gh-surface); border: 1px solid var(--gh-border); padding: 7px 12px; text-align: left; color: var(--gh-muted); font-weight: 600; font-size: 12px; }
td { border: 1px solid var(--gh-border); padding: 7px 12px; color: var(--gh-text); }
tr:nth-child(even) td { background: #0d1117; } tr:nth-child(odd) td { background: #161b22; }
.blockquote { border-left: 3px solid var(--gh-accent); padding: 8px 14px; background: #1c2128; border-radius: 0 4px 4px 0; color: var(--gh-text); margin: 12px 0; font-size: 13px; }
.blockquote strong { color: var(--gh-yellow); }
.warning-box { border: 1px solid #f85149; border-left: 4px solid #f85149; background: #1c1010; padding: 10px 14px; border-radius: 0 6px 6px 0; margin: 14px 0; font-size: 13px; }
.warning-box strong { color: var(--gh-red); }
.step-flow { display: flex; flex-direction: column; gap: 6px; margin: 10px 0; }
.step { display: flex; align-items: flex-start; gap: 10px; font-size: 13px; }
.step-num { min-width: 24px; height: 24px; border-radius: 50%; background: #21262d; border: 1px solid var(--gh-border); color: var(--gh-accent); font-size: 11px; font-weight: 700; display: flex; align-items: center; justify-content: center; }
.file-tree { background: var(--gh-surface); border: 1px solid var(--gh-border); border-radius: 6px; overflow: hidden; margin: 10px 0; }
.file-tree-header { background: #21262d; padding: 8px 14px; font-size: 12px; color: var(--gh-muted); border-bottom: 1px solid var(--gh-border); display: flex; align-items: center; gap: 6px; }
.file-row { display: flex; align-items: center; gap: 8px; padding: 6px 14px; border-bottom: 1px solid var(--gh-border); font-size: 13px; color: var(--gh-text); }
.file-row:last-child { border-bottom: none; }
.file-row i { color: var(--gh-muted); font-size: 15px; }
.file-row a { color: var(--gh-accent); text-decoration: none; }
.file-row a:hover { text-decoration: underline; }
.file-row .file-desc { margin-left: auto; color: var(--gh-muted); font-size: 12px; }
.script-link-box { background: #21262d; border: 1px solid var(--gh-border); border-radius: 6px; padding: 14px 16px; display: flex; align-items: center; gap: 12px; margin: 10px 0; }
.script-link-box i { font-size: 22px; color: var(--gh-purple); }
.script-link-box .info { display: flex; flex-direction: column; gap: 2px; }
.script-link-box .info a { color: var(--gh-accent); font-size: 14px; font-weight: 600; text-decoration: none; }
.script-link-box .info a:hover { text-decoration: underline; }
.script-link-box .info span { color: var(--gh-muted); font-size: 12px; }
.avatar { width: 40px; height: 40px; border-radius: 50%; background: #1f6feb; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; color: #fff; border: 2px solid var(--gh-border); }
.contrib-info { font-size: 13px; }
.contrib-info strong { color: var(--gh-text); }
.contrib-info span { color: var(--gh-muted); display: block; font-size: 12px; }
</style>

<div class="wrap">
  <div class="repo-header">
    <i class="ti ti-brand-github" aria-hidden="true"></i>
    Sael2727 / <span style="color:var(--gh-text)">SaelGermanGarcia_2025-0725_DHCP-Starvation</span>
  </div>
  <p class="repo-desc">Práctica de seguridad de redes — Ataque DHCP Starvation con Scapy sobre entorno multi-VLAN (EVE-NG). Uso exclusivamente educativo — ITLA 2026.</p>

  <div class="badges">
    <span class="badge"><span class="badge-label">Python</span><span class="badge-value b-blue">3.x</span></span>
    <span class="badge"><span class="badge-label">Scapy</span><span class="badge-value b-green">Latest</span></span>
    <span class="badge"><span class="badge-label">Platform</span><span class="badge-value b-gray">Linux</span></span>
    <span class="badge"><span class="badge-label">VLAN</span><span class="badge-value b-orange">10 · 20</span></span>
    <span class="badge"><span class="badge-label">Uso</span><span class="badge-value b-red">Educativo</span></span>
    <span class="badge"><span class="badge-label">Asignatura</span><span class="badge-value b-purple">Seguridad de Redes</span></span>
  </div>

  <hr>

  <h2><i class="ti ti-target" aria-hidden="true" style="font-size:16px;vertical-align:-2px;margin-right:6px;color:var(--gh-red)"></i>Objetivo del laboratorio</h2>
  <p>Analizar el comportamiento de los servidores DHCP legítimos cuando son sometidos a un <strong>ataque de agotamiento de recursos (DHCP Starvation / DHCP Exhaustion)</strong>. Mediante la simulación de múltiples clientes falsos con MAC spoofing, se consume la totalidad del pool de direcciones IP del servidor R1, generando una <span class="red">Denegación de Servicio (DoS)</span> que impide a los usuarios legítimos conectarse.</p>

  <div class="blockquote"><strong>Video demo:</strong> <a href="https://youtube.com/playlist?list=PLV_dKVnYXf6dpmk3j8uXPHAZdbrkCQGAY" style="color:var(--gh-accent)">youtube.com/playlist — PLV_dKVnYXf6...</a></div>

  <h2><i class="ti ti-topology-star" aria-hidden="true" style="font-size:16px;vertical-align:-2px;margin-right:6px;color:var(--gh-accent)"></i>Topología de red</h2>

  <h3>Segmentación de VLANs</h3>
  <table>
    <tr><th>VLAN ID</th><th>Nombre</th><th>Segmento IP</th><th>Descripción</th></tr>
    <tr><td><code>10</code></td><td>Usuarios</td><td><code>10.7.25.0/24</code></td><td>VPC1 — Pool objetivo del agotamiento</td></tr>
    <tr><td><code>20</code></td><td>Servidores</td><td><code>10.7.20.0/24</code></td><td>VPC2 — Pool objetivo del agotamiento</td></tr>
    <tr><td><code>Trunk</code></td><td>Inter-VLAN</td><td>Múltiple</td><td><code>e0/3</code> de SW1 en modo Trunk dot1q para el atacante</td></tr>
  </table>

  <h3>Matriz de direccionamiento IP</h3>
  <table>
    <tr><th>Elemento / Rol</th><th>Dirección IP</th><th>Interfaz</th><th>Estado</th></tr>
    <tr><td>Servidor DHCP (R1)</td><td><code>10.7.25.1 / 10.7.20.1</code></td><td><code>Eth0/0.10 · .20</code></td><td><span class="orange">Vulnerable — Pool agotable</span></td></tr>
    <tr><td>Atacante</td><td>Múltiple</td><td><code>ens4.10 · ens4.20</code></td><td><span class="red">Flooding masivo activo</span></td></tr>
    <tr><td>Víctima (VPC1 / VPC2)</td><td>Dinámica</td><td><code>eth0</code></td><td><span class="red">DoS — Can't find dhcp server</span></td></tr>
  </table>

  <h2><i class="ti ti-settings" aria-hidden="true" style="font-size:16px;vertical-align:-2px;margin-right:6px;color:var(--gh-green)"></i>Requisitos y configuración previa</h2>

  <h3>Dependencias</h3>
  <div class="code-header"><i class="ti ti-terminal" aria-hidden="true"></i> bash</div>
  <pre><span class="green">sudo</span> apt update && <span class="green">sudo</span> apt install -y python3-scapy python3-pip
<span class="muted"># Privilegios root requeridos para sendp()</span></pre>

  <h3>Trunk en SW1 (Cisco IOS)</h3>
  <div class="code-header"><i class="ti ti-router" aria-hidden="true"></i> cisco-ios</div>
  <pre>SW1(config)# interface ethernet0/3
SW1(config-if)# switchport trunk encapsulation dot1q
SW1(config-if)# switchport mode trunk
SW1(config-if)# no shutdown
SW1(config-if)# end
SW1# write memory</pre>

  <h3>Subinterfaces 802.1Q en el atacante</h3>
  <div class="code-header"><i class="ti ti-terminal" aria-hidden="true"></i> bash</div>
  <pre><span class="green">sudo</span> ip link add link ens4 name ens4.10 type vlan id 10
<span class="green">sudo</span> ip link add link ens4 name ens4.20 type vlan id 20
<span class="green">sudo</span> ip link set ens4.10 up && <span class="green">sudo</span> ip link set ens4.20 up
<span class="green">sudo</span> ip addr add 10.7.25.50/24 dev ens4.10
<span class="green">sudo</span> ip addr add 10.7.20.50/24 dev ens4.20</pre>

  <h2><i class="ti ti-player-play" aria-hidden="true" style="font-size:16px;vertical-align:-2px;margin-right:6px;color:var(--gh-accent)"></i>Uso</h2>
  <div class="code-header"><i class="ti ti-terminal" aria-hidden="true"></i> bash</div>
  <pre><span class="muted"># Ejecutar el ataque (2000 paquetes por interfaz)</span>
<span class="green">sudo</span> python3 dhcp_starvation.py 2000

<span class="muted"># Verificar colapso del pool en R1</span>
R1# show ip dhcp pool
R1# show ip dhcp binding

<span class="muted"># Verificar DoS en la víctima</span>
VPCS&gt; ip dhcp
<span class="red">DDD Can't find dhcp server</span></pre>

  <h2><i class="ti ti-code" aria-hidden="true" style="font-size:16px;vertical-align:-2px;margin-right:6px;color:var(--gh-purple)"></i>Funcionamiento del script</h2>

  <div class="step-flow">
    <div class="step"><div class="step-num">1</div><div><code>INTERFACES</code> — Define <code>ens4.10</code> y <code>ens4.20</code> como objetivos simultáneos del flooding.</div></div>
    <div class="step"><div class="step-num">2</div><div><code>random_mac()</code> — Genera una MAC Unicast aleatoria por paquete (<code>& 0xFC</code> en el primer octeto).</div></div>
    <div class="step"><div class="step-num">3</div><div><code>mac_to_bytes(mac)</code> — Convierte la MAC a bytes para poblar el campo <code>chaddr</code> en BOOTP.</div></div>
    <div class="step"><div class="step-num">4</div><div><code>flood_iface(iface, count)</code> — Construye y envía paquetes <code>Ether / IP / UDP / BOOTP / DHCP Discover</code> con <code>sendp()</code>.</div></div>
    <div class="step"><div class="step-num">5</div><div><code>dhcp_starvation(count)</code> — Lanza hilos paralelos (<code>threading</code>) por VLAN, multiplicando la velocidad del ataque.</div></div>
  </div>

  <h3>Código fuente</h3>
  <div class="script-link-box">
    <i class="ti ti-file-code" aria-hidden="true"></i>
    <div class="info">
      <a href="https://github.com/Sael2727/SaelGermanGarcia_2025-0725_DHCP-Starvation/blob/main/dhcp_starvation.py">dhcp_starvation.py</a>
      <span>Ver script completo en el repositorio</span>
    </div>
    <i class="ti ti-external-link" aria-hidden="true" style="margin-left:auto;color:var(--gh-muted);font-size:16px;"></i>
  </div>

  <h2><i class="ti ti-shield-check" aria-hidden="true" style="font-size:16px;vertical-align:-2px;margin-right:6px;color:var(--gh-green)"></i>Contramedidas y mitigación (Cisco IOS)</h2>

  <h3>Port Security — limitar MACs por puerto</h3>
  <div class="code-header"><i class="ti ti-router" aria-hidden="true"></i> cisco-ios</div>
  <pre>SW1(config)# interface ethernet0/3
SW1(config-if)# switchport port-security
SW1(config-if)# switchport port-security maximum 2
SW1(config-if)# switchport port-security violation restrict
SW1(config-if)# exit</pre>

  <h3>DHCP Snooping — rate limiting</h3>
  <div class="code-header"><i class="ti ti-router" aria-hidden="true"></i> cisco-ios</div>
  <pre>SW1(config)# ip dhcp snooping
SW1(config)# ip dhcp snooping vlan 10,20
SW1(config)# interface range ethernet0/1-3
SW1(config-if-range)# ip dhcp snooping limit rate 10</pre>

  <h2><i class="ti ti-folder" aria-hidden="true" style="font-size:16px;vertical-align:-2px;margin-right:6px;color:var(--gh-yellow)"></i>Archivos del repositorio</h2>

  <div class="file-tree">
    <div class="file-tree-header"><i class="ti ti-folder-open" aria-hidden="true"></i> SaelGermanGarcia_2025-0725_DHCP-Starvation</div>
    <div class="file-row"><i class="ti ti-folder" aria-hidden="true"></i><a href="#">Capturas de Pantalla DHCP Starvation/</a><span class="file-desc">Screenshots operacionales</span></div>
    <div class="file-row" style="padding-left:30px;"><i class="ti ti-photo" aria-hidden="true"></i><span>Agotamiento Total de los Pools DHCP en el Gateway2.png</span></div>
    <div class="file-row" style="padding-left:30px;"><i class="ti ti-photo" aria-hidden="true"></i><span>Denegación de Servicio (DoS) Efectiva en el Cliente Víctima.png</span></div>
    <div class="file-row" style="padding-left:30px;"><i class="ti ti-photo" aria-hidden="true"></i><span>Ejecución y Despliegue Masivo del Ataque DHCP Starvation.png</span></div>
    <div class="file-row" style="padding-left:30px;"><i class="ti ti-photo" aria-hidden="true"></i><span>Ejecución y Despliegue Masivo.png</span></div>
    <div class="file-row" style="padding-left:30px;"><i class="ti ti-photo" aria-hidden="true"></i><span>Saturación de la Tabla de Asignaciones Lógicas (DHCP Bindings).png</span></div>
    <div class="file-row" style="padding-left:30px;"><i class="ti ti-photo" aria-hidden="true"></i><span>Saturación de la Tabla de Asignaciones Lógicas (DHCP Bindings)2.png</span></div>
    <div class="file-row" style="padding-left:30px;"><i class="ti ti-photo" aria-hidden="true"></i><span>contramedidass.png</span></div>
    <div class="file-row"><i class="ti ti-file-code" aria-hidden="true" style="color:var(--gh-purple)"></i><a href="https://github.com/Sael2727/SaelGermanGarcia_2025-0725_DHCP-Starvation/blob/main/dhcp_starvation.py">dhcp_starvation.py</a><span class="file-desc">Script principal del ataque</span></div>
    <div class="file-row"><i class="ti ti-file-type-pdf" aria-hidden="true" style="color:var(--gh-red)"></i><span>SaelGermanGarcia_2025-0725_DHCP_Starvation_P1.pdf</span><span class="file-desc">Documentación técnica completa</span></div>
    <div class="file-row"><i class="ti ti-file-text" aria-hidden="true" style="color:var(--gh-green)"></i><span>README.md</span><span class="file-desc">Este archivo</span></div>
  </div>

  <h2><i class="ti ti-book" aria-hidden="true" style="font-size:16px;vertical-align:-2px;margin-right:6px;color:var(--gh-muted)"></i>Referencias</h2>
  <p style="font-size:13px; color:var(--gh-muted);">
    1. Cisco Systems. <em>DHCP Snooping &amp; Port Security Configuration Guide</em>. Documentación oficial Cisco IOS.<br>
    2. Scapy Project. <em>Scapy: Interactive packet manipulation program</em>. <a href="https://scapy.net" class="accent">scapy.net</a><br>
    3. IETF. <em>RFC 2131: Dynamic Host Configuration Protocol</em>. Especificación base del protocolo DHCP.<br>
    4. Reconocimiento especial: troubleshooting, base del script y documentación apoyados en Inteligencia Artificial.
  </p>

  <hr>

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
    <div class="avatar">SG</div>
    <div class="contrib-info">
      <strong>Sael Germán García</strong>
      <span>Matrícula: 2025-0725 · ITLA 2026</span>
      <span>Asignatura: Seguridad de Redes · Prof. Jonathan Rondón</span>
    </div>
  </div>

  <div class="warning-box">
    <strong>⚠ AVISO LEGAL</strong><br>
    Este repositorio fue desarrollado exclusivamente con fines académicos y educativos dentro del Instituto Tecnológico de las Américas (ITLA). Su uso en redes sin autorización explícita es ilegal y éticamente inaceptable.
  </div>
</div>
