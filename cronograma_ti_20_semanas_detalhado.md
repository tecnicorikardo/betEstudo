## Módulo I – Fundamentos e Manutenção de Hardware

### Semana 1 – Fundamentos de Hardware (parte 1)

#### Segunda-feira: O que é hardware? Diferença entre hardware e software. Componentes internos básicos (placa-mãe, CPU, memória RAM, HD/SSD).

**Hardware** refere-se à parte física e tangível de um computador ou sistema eletrônico. São todos os componentes que podemos tocar e ver, como a tela, o teclado, o mouse, e as peças internas como a placa-mãe, o processador, a memória e os dispositivos de armazenamento. É a estrutura que permite que o sistema funcione.

**Software**, por outro lado, é a parte lógica e intangível. São os programas, aplicativos, sistemas operacionais e dados que instruem o hardware sobre o que fazer. Sem o software, o hardware seria apenas um conjunto de peças sem utilidade. A interação entre hardware e software é fundamental para o funcionamento de qualquer sistema computacional.

**Componentes Internos Básicos:**
*   **Placa-Mãe (Motherboard):** É a principal placa de circuito impresso do computador, que conecta e permite a comunicação entre todos os outros componentes. Ela contém o chipset, slots para memória RAM, slots de expansão (PCIe), portas USB, e o soquete para o processador.
*   **CPU (Central Processing Unit - Unidade Central de Processamento):** Conhecido como o 
cérebro do computador. Ele executa as instruções dos programas, realiza cálculos e processa dados. Sua velocidade é medida em Hertz (Hz), geralmente em Gigahertz (GHz).
*   **Memória RAM (Random Access Memory):** É uma memória volátil de acesso rápido que armazena temporariamente os dados e programas que estão sendo usados ativamente pelo CPU. Quanto mais RAM, mais programas podem ser executados simultaneamente sem lentidão.
*   **HD/SSD (Hard Disk Drive / Solid State Drive):** São dispositivos de armazenamento permanente. O HDD é um disco magnético com partes móveis, enquanto o SSD utiliza memória flash, sendo mais rápido, silencioso e resistente a impactos. Ambos armazenam o sistema operacional, programas e arquivos do usuário.

#### Terça-feira: Arquitetura de um computador: barramentos, chipset, clock. Função de cada componente.

A **arquitetura de um computador** descreve como os componentes de hardware são interconectados e como eles trabalham juntos para executar tarefas. Os principais elementos dessa arquitetura incluem:

*   **Barramentos (Buses):** São vias de comunicação que permitem a troca de dados entre os diferentes componentes do computador. Existem vários tipos de barramentos, como o barramento de dados (transporta os dados), o barramento de endereços (indica a localização dos dados na memória) e o barramento de controle (gerencia o fluxo de informações).
*   **Chipset:** É um conjunto de chips na placa-mãe que atua como um "controlador de tráfego", gerenciando a comunicação entre o CPU, a memória, os dispositivos de armazenamento e os periféricos. Geralmente é dividido em Northbridge (controla CPU, RAM e placa de vídeo) e Southbridge (controla dispositivos de E/S mais lentos como USB, SATA, áudio).
*   **Clock (Relógio):** É um sinal eletrônico que sincroniza as operações de todos os componentes do computador. A frequência do clock, medida em Hertz (Hz), determina a velocidade com que o CPU e outros componentes executam suas tarefas. Um clock mais rápido geralmente significa um desempenho mais rápido.

**Função de cada componente:**
*   **CPU:** Executa instruções, realiza cálculos e processa dados.
*   **Memória RAM:** Armazena temporariamente dados e programas em uso para acesso rápido pelo CPU.
*   **Placa-Mãe:** Conecta e permite a comunicação entre todos os componentes do sistema.
*   **HD/SSD:** Armazena permanentemente o sistema operacional, programas e arquivos.
*   **Placa de Vídeo (GPU):** Processa e renderiza imagens e vídeos para exibição no monitor. Pode ser integrada ao CPU ou uma placa dedicada.
*   **Fonte de Alimentação:** Converte a corrente alternada (AC) da tomada em corrente contínua (DC) para alimentar todos os componentes do computador.

#### Quarta-feira: Processadores: evolução (CISC x RISC), arquitetura multicore, hyper-threading. Como escolher um CPU.

Os **processadores (CPUs)** são o coração do computador, responsáveis por executar as instruções. Sua evolução tem sido marcada por diversas inovações:

*   **CISC (Complex Instruction Set Computer) vs. RISC (Reduced Instruction Set Computer):**
    *   **CISC:** Processadores com um conjunto de instruções complexas, onde uma única instrução pode realizar várias operações de baixo nível. Exemplos incluem os processadores Intel x86. Eles são mais flexíveis, mas podem ser mais lentos devido à complexidade das instruções.
    *   **RISC:** Processadores com um conjunto de instruções reduzidas e mais simples, onde cada instrução executa uma única operação. Exemplos incluem ARM. Eles são mais eficientes em termos de energia e podem ser mais rápidos para certas tarefas devido à simplicidade e paralelização.

*   **Arquitetura Multicore:** Em vez de ter um único núcleo de processamento, os CPUs modernos possuem múltiplos núcleos (dual-core, quad-core, hexa-core, octa-core, etc.). Cada núcleo pode executar tarefas de forma independente, permitindo que o computador execute várias operações simultaneamente, melhorando o desempenho em multitarefas e aplicativos que suportam paralelismo.

*   **Hyper-threading (ou Multithreading Simultâneo - SMT):** É uma tecnologia da Intel (e equivalente em outras arquiteturas) que permite que cada núcleo físico do CPU execute duas threads (sequências de instruções) simultaneamente. Isso faz com que o sistema operacional "veja" o dobro de núcleos lógicos, otimizando o uso dos recursos do processador e melhorando o desempenho em cargas de trabalho que se beneficiam de mais threads.

**Como escolher um CPU:**
Ao escolher um CPU, considere os seguintes fatores:
*   **Uso:** Para tarefas básicas (navegação, e-mail), um CPU de entrada é suficiente. Para jogos, edição de vídeo ou tarefas pesadas, um CPU de alto desempenho com mais núcleos e threads é ideal.
*   **Geração e Modelo:** Processadores mais recentes geralmente oferecem melhor desempenho e eficiência energética. Compare modelos dentro da mesma geração (ex: Intel Core i5-13600K vs. AMD Ryzen 7 7700X).
*   **Número de Núcleos e Threads:** Mais núcleos e threads são benéficos para multitarefas e aplicativos que utilizam paralelismo.
*   **Frequência (Clock):** Uma frequência de clock mais alta pode significar melhor desempenho em tarefas que dependem de um único núcleo.
*   **Cache:** Memória cache (L1, L2, L3) é uma memória muito rápida integrada ao CPU que armazena dados frequentemente acessados, reduzindo o tempo de acesso à RAM.
*   **Compatibilidade:** Verifique a compatibilidade do soquete do CPU com a placa-mãe (ex: LGA 1700 para Intel, AM5 para AMD).
*   **Preço:** Equilibre o desempenho desejado com o orçamento disponível.

#### Quinta-feira: Memórias: RAM (DDR, frequência, latência), cache L1/L2/L3, memória virtual. Swapping.

As **memórias** são cruciais para o desempenho do computador, armazenando dados e instruções para acesso rápido pelo CPU. Existem diferentes tipos e conceitos importantes:

*   **Memória RAM (Random Access Memory):** É a memória principal do sistema, onde os dados e programas em execução são armazenados temporariamente. É volátil, ou seja, perde seu conteúdo quando o computador é desligado. As características importantes da RAM incluem:
    *   **DDR (Double Data Rate):** Refere-se à tecnologia que permite a transferência de dados duas vezes por ciclo de clock. As gerações mais comuns são DDR4 e DDR5, com DDR5 sendo a mais recente e mais rápida.
    *   **Frequência:** Medida em MHz (megahertz), indica a velocidade com que a memória pode transferir dados. Uma frequência mais alta geralmente resulta em melhor desempenho.
    *   **Latência (CAS Latency - CL):** É o tempo que a memória leva para responder a uma solicitação do CPU. Medida em ciclos de clock, um valor de latência menor indica uma memória mais rápida.

*   **Memória Cache (L1/L2/L3):** São pequenas quantidades de memória muito rápida, integradas ao CPU ou próximas a ele, que armazenam dados e instruções frequentemente acessados. Elas atuam como um buffer entre o CPU e a RAM, reduzindo o tempo de acesso aos dados e acelerando o processamento. Existem três níveis:
    *   **L1 Cache:** A menor e mais rápida, integrada diretamente em cada núcleo do CPU.
    *   **L2 Cache:** Maior que a L1, pode ser dedicada a cada núcleo ou compartilhada entre alguns núcleos.
    *   **L3 Cache:** A maior e mais lenta das caches, geralmente compartilhada por todos os núcleos do CPU.

*   **Memória Virtual:** É uma técnica de gerenciamento de memória que permite que um sistema operacional compense a falta de memória RAM física, usando parte do espaço de armazenamento (HD/SSD) como se fosse RAM. Isso permite que o sistema execute programas maiores do que a RAM disponível, mas com um custo de desempenho, pois o acesso ao disco é muito mais lento que o acesso à RAM.

*   **Swapping (Paginação):** É o processo pelo qual o sistema operacional move blocos de dados (páginas) entre a RAM e o disco rígido (arquivo de paginação ou swap file) quando a memória física está cheia. Quando um programa precisa de dados que estão no disco (swapped out), o sistema precisa trazê-los de volta para a RAM (swapped in), o que causa uma lentidão perceptível conhecida como "thrashing" se ocorrer com muita frequência.

#### Sexta-feira: Armazenamento: HDD (setores, trilhas, tempo de busca) vs SSD (SATA, NVMe, controlador). RAID 0,1,5,10.

Os dispositivos de **armazenamento** são essenciais para guardar dados de forma permanente. Os dois tipos principais são HDD e SSD, com tecnologias e características distintas:

*   **HDD (Hard Disk Drive):** É um dispositivo de armazenamento mecânico que utiliza discos magnéticos giratórios (platters) para armazenar dados. As informações são gravadas em:
    *   **Trilhas (Tracks):** Círculos concêntricos nos platters.
    *   **Setores (Sectors):** Pequenas divisões das trilhas, que são a menor unidade de armazenamento.
    *   **Tempo de Busca (Seek Time):** É o tempo que a cabeça de leitura/gravação leva para se mover para a trilha correta. É um dos fatores que limitam a velocidade do HDD.
    *   **Latência Rotacional:** Tempo que o setor desejado leva para girar e passar sob a cabeça de leitura/gravação.
    HDDs são mais baratos por gigabyte e têm maior capacidade, mas são mais lentos e suscetíveis a danos físicos.

*   **SSD (Solid State Drive):** É um dispositivo de armazenamento que utiliza memória flash (semelhante a um pendrive grande) para armazenar dados, sem partes móveis. Isso os torna muito mais rápidos, silenciosos, eficientes em energia e resistentes a impactos em comparação com os HDDs. Os SSDs se conectam ao sistema de diferentes formas:
    *   **SATA (Serial Advanced Technology Attachment):** Interface mais comum, com velocidades de até 600 MB/s. Compatível com a maioria das placas-mãe mais antigas e recentes.
    *   **NVMe (Non-Volatile Memory Express):** Protocolo de comunicação projetado especificamente para SSDs baseados em PCIe, oferecendo velocidades significativamente maiores (vários GB/s). Requer um slot M.2 na placa-mãe.
    *   **Controlador:** É o "cérebro" do SSD, responsável por gerenciar a memória flash, otimizar o desempenho e garantir a integridade dos dados.

*   **RAID (Redundant Array of Independent Disks):** É uma tecnologia que combina múltiplos discos rígidos (HDDs ou SSDs) em uma única unidade lógica para melhorar o desempenho, a redundância ou ambos. Os níveis de RAID mais comuns incluem:
    *   **RAID 0 (Striping):** Distribui os dados em blocos por vários discos. Oferece maior desempenho (leitura/escrita mais rápida), mas não oferece redundância; a falha de um disco resulta na perda de todos os dados.
    *   **RAID 1 (Mirroring):** Duplica os dados em dois ou mais discos. Oferece alta redundância (se um disco falhar, os dados ainda estão no outro), mas o desempenho é similar ao de um único disco e a capacidade utilizável é reduzida pela metade.
    *   **RAID 5 (Striping with Parity):** Distribui os dados e informações de paridade (para recuperação de dados) por três ou mais discos. Oferece bom equilíbrio entre desempenho e redundância (pode tolerar a falha de um disco sem perda de dados).
    *   **RAID 10 (ou RAID 1+0):** Combina RAID 1 e RAID 0. Cria espelhamentos de conjuntos de discos que são então distribuídos. Oferece alto desempenho e alta redundância (pode tolerar a falha de múltiplos discos, desde que não sejam do mesmo espelhamento), mas é mais caro devido ao maior número de discos necessários.

---
### Semana 2 – Fundamentos de Hardware (parte 2) + Introdução à Informática

#### Segunda-feira: Placa-mãe: soquetes, chipsets (Z, B, H), capacitores, VRM. BIOS/UEFI.

A **placa-mãe**, também conhecida como *motherboard*, é o componente central que interliga e permite a comunicação entre todos os outros dispositivos de hardware do computador. Ela é essencial para o funcionamento do sistema e possui diversas características importantes:

*   **Soquetes (Sockets):** São os encaixes físicos na placa-mãe onde o processador (CPU) é instalado. Cada tipo de processador (Intel ou AMD) e geração específica exige um tipo de soquete compatível (ex: LGA 1700 para Intel, AM5 para AMD). A incompatibilidade do soquete impede a instalação do CPU.

*   **Chipsets (Z, B, H):** O chipset é um conjunto de circuitos integrados na placa-mãe que gerencia a comunicação entre o CPU e os demais componentes (memória, armazenamento, periféricos). Os chipsets da Intel, por exemplo, são categorizados em séries como Z, B e H, que indicam diferentes níveis de funcionalidade e recursos:
    *   **Série Z (ex: Z790):** Chipsets de alto desempenho, geralmente para CPUs de ponta, que permitem *overclocking* (aumento da frequência de operação do CPU e da memória) e oferecem mais linhas PCIe para placas de vídeo e SSDs NVMe.
    *   **Série B (ex: B760):** Chipsets de médio alcance, que oferecem um bom equilíbrio entre custo e funcionalidade, sem suporte a *overclocking* do CPU, mas com recursos suficientes para a maioria dos usuários.
    *   **Série H (ex: H610):** Chipsets de entrada, mais básicos e econômicos, ideais para sistemas de escritório ou uso doméstico leve, com menos portas e recursos.

*   **Capacitores:** São componentes eletrônicos que armazenam energia elétrica temporariamente. Na placa-mãe, eles são cruciais para filtrar ruídos elétricos e fornecer energia estável aos componentes, especialmente ao CPU. Capacitores de boa qualidade (sólidos) contribuem para a estabilidade e longevidade da placa-mãe.

*   **VRM (Voltage Regulator Module - Módulo Regulador de Tensão):** É um circuito na placa-mãe responsável por fornecer a tensão correta e estável para o CPU. Um VRM robusto é fundamental para o desempenho e a estabilidade do processador, especialmente em situações de alta carga ou *overclocking*.

*   **BIOS/UEFI (Basic Input/Output System / Unified Extensible Firmware Interface):** São firmwares (software gravado em um chip na placa-mãe) que inicializam o hardware do computador quando ele é ligado. O BIOS é a versão mais antiga, enquanto o UEFI é o padrão moderno, oferecendo uma interface gráfica mais amigável, suporte a discos maiores (GPT), inicialização mais rápida e recursos de segurança aprimorados.

#### Terça-feira: Periféricos e conectores: USB (tipos e velocidades), HDMI, DisplayPort, Thunderbolt. Fontes de alimentação (certificação 80 Plus, eficiência).

Os **periféricos** são dispositivos externos que se conectam ao computador para expandir suas funcionalidades (ex: teclado, mouse, monitor, impressora). A conexão desses periféricos é feita através de diversos **conectores** e padrões:

*   **USB (Universal Serial Bus):** É o padrão mais comum para conectar uma vasta gama de periféricos. Evoluiu em tipos e velocidades:
    *   **USB-A:** O conector retangular padrão, presente na maioria dos computadores.
    *   **USB-B:** Geralmente usado em impressoras e outros dispositivos maiores.
    *   **USB-C:** Conector reversível e compacto, que se tornou padrão em muitos dispositivos modernos, suportando altas velocidades e entrega de energia.
    *   **Versões e Velocidades:**
        *   **USB 2.0:** Até 480 Mbps (Megabits por segundo).
        *   **USB 3.0/3.1 Gen 1/3.2 Gen 1:** Até 5 Gbps (Gigabits por segundo).
        *   **USB 3.1 Gen 2/3.2 Gen 2:** Até 10 Gbps.
        *   **USB 3.2 Gen 2x2:** Até 20 Gbps.
        *   **USB4:** Até 40 Gbps.

*   **HDMI (High-Definition Multimedia Interface):** Padrão para transmissão de áudio e vídeo digital de alta qualidade. Amplamente utilizado para conectar monitores, TVs e projetores.

*   **DisplayPort:** Outro padrão para transmissão de áudio e vídeo digital, frequentemente encontrado em monitores de alto desempenho e placas de vídeo. Oferece recursos como taxas de atualização mais altas e suporte a múltiplos monitores.

*   **Thunderbolt:** Tecnologia desenvolvida pela Intel que combina PCI Express e DisplayPort em um único cabo, oferecendo altíssimas velocidades de transferência de dados (até 40 Gbps no Thunderbolt 4) e capacidade de encadeamento de dispositivos. Utiliza o conector USB-C.

**Fontes de Alimentação:** A fonte de alimentação (PSU - Power Supply Unit) é responsável por converter a corrente alternada (AC) da tomada em corrente contínua (DC) nas tensões adequadas para alimentar todos os componentes do computador.

*   **Certificação 80 Plus:** É um programa de certificação que garante a eficiência energética de uma fonte de alimentação. As fontes certificadas 80 Plus (White, Bronze, Silver, Gold, Platinum, Titanium) garantem que a fonte converte pelo menos 80% da energia da tomada em energia útil para o computador, dissipando menos calor e economizando energia. Quanto maior o nível da certificação, maior a eficiência.

*   **Eficiência:** Uma fonte mais eficiente desperdiça menos energia na forma de calor, o que resulta em menor consumo de eletricidade, menor aquecimento interno do sistema e, consequentemente, menor necessidade de refrigeração.

#### Quarta-feira: Manutenção de hardware: limpeza preventiva, troca de pasta térmica, diagnóstico de falhas (beeps, POST, erros comuns).

A **manutenção de hardware** é fundamental para garantir a longevidade, o desempenho e a estabilidade do computador. Ela envolve tanto ações preventivas quanto corretivas:

*   **Limpeza Preventiva:** A acumulação de poeira e sujeira é uma das principais causas de superaquecimento e falhas de componentes. A limpeza regular inclui:
    *   **Limpeza interna:** Utilizar ar comprimido para remover poeira de ventoinhas (CPU, placa de vídeo, fonte), dissipadores de calor e componentes da placa-mãe. É importante segurar as ventoinhas para que não girem excessivamente durante a limpeza.
    *   **Limpeza externa:** Limpar o gabinete, teclado, mouse e monitor com panos macios e produtos específicos, evitando líquidos diretamente nos componentes.

*   **Troca de Pasta Térmica:** A pasta térmica é um composto aplicado entre o CPU (ou GPU) e o dissipador de calor para melhorar a transferência de calor. Com o tempo, ela pode secar e perder sua eficácia, levando ao superaquecimento. A troca periódica (a cada 1-3 anos, dependendo do uso e da qualidade da pasta) é crucial para manter as temperaturas do processador sob controle.

*   **Diagnóstico de Falhas:** Quando o computador apresenta problemas, é importante saber como diagnosticar a causa. Alguns sinais comuns e métodos de diagnóstico incluem:
    *   **Beeps (Sons da BIOS):** Ao ligar, a BIOS/UEFI emite uma sequência de bipes se houver algum problema. Cada sequência de bipes corresponde a um código de erro específico (ex: problema de memória, placa de vídeo, CPU). Consultar o manual da placa-mãe é essencial para interpretar esses códigos.
    *   **POST (Power-On Self-Test):** É um processo de autoteste que o computador realiza ao ser ligado para verificar se os componentes essenciais (CPU, RAM, placa de vídeo) estão funcionando corretamente. Se o POST falhar, o sistema não inicializa e pode emitir bipes.
    *   **Erros Comuns:**
        *   **Tela Azul da Morte (BSOD - Blue Screen of Death):** No Windows, indica um erro crítico do sistema, geralmente relacionado a drivers, hardware ou software. O código de erro exibido pode ajudar a identificar a causa.
        *   **Não Liga/Não Dá Vídeo:** Pode ser problema na fonte de alimentação, memória RAM mal encaixada ou defeituosa, placa de vídeo, ou CPU.
        *   **Superaquecimento:** Causa desligamentos inesperados, lentidão e pode danificar componentes. Verificar ventoinhas, limpeza e pasta térmica.
        *   **Lentidão:** Pode ser causada por vírus, disco cheio, pouca RAM, ou problemas de hardware.

#### Quinta-feira: Introdução à Informática: história dos computadores (gerações), Lei de Moore. Sistemas numéricos: binário, hexadecimal, conversões.

A **Informática** é a ciência que estuda o tratamento automático e racional da informação. Para entender seu funcionamento, é fundamental conhecer sua história e os princípios básicos de representação de dados:

*   **História dos Computadores (Gerações):** A evolução dos computadores é dividida em gerações, marcadas por avanços tecnológicos significativos:
    *   **1ª Geração (1940s-1950s):** Válvulas eletrônicas. Computadores grandes, caros, lentos e que geravam muito calor (ex: ENIAC).
    *   **2ª Geração (1950s-1960s):** Transistores. Menores, mais rápidos, mais eficientes e confiáveis que as válvulas.
    *   **3ª Geração (1960s-1970s):** Circuitos Integrados (CIs). Vários transistores em um único chip. Surgimento dos minicomputadores.
    *   **4ª Geração (1970s-1980s):** Microprocessadores (CIs em larga escala). Início dos computadores pessoais (PCs).
    *   **5ª Geração (1980s-presente):** Inteligência Artificial, processamento paralelo, redes neurais. Foco em interfaces mais intuitivas e computação distribuída.

*   **Lei de Moore:** Proposta por Gordon Moore (cofundador da Intel) em 1965, afirma que o número de transistores em um circuito integrado dobraria a cada dois anos (originalmente 18 meses). Embora não seja uma lei física, tem sido uma observação empírica que impulsionou a indústria de semicondutores por décadas, resultando em computadores cada vez mais poderosos e baratos. Atualmente, seu ritmo tem desacelerado, mas o conceito de miniaturização e aumento de desempenho continua relevante.

*   **Sistemas Numéricos:** Computadores operam com base em sistemas numéricos diferentes do decimal (base 10) que usamos no dia a dia:
    *   **Sistema Binário (Base 2):** Utiliza apenas dois dígitos: 0 e 1. É a linguagem fundamental dos computadores, onde 0 representa "desligado" e 1 representa "ligado".
    *   **Sistema Hexadecimal (Base 16):** Utiliza 16 dígitos: 0-9 e A-F. É frequentemente usado em programação e redes para representar grandes números binários de forma mais compacta e legível (cada dígito hexadecimal corresponde a 4 dígitos binários).

*   **Conversões entre Sistemas Numéricos:** É essencial saber converter números entre esses sistemas:
    *   **Decimal para Binário:** Dividir o número decimal sucessivamente por 2 e anotar os restos na ordem inversa.
    *   **Binário para Decimal:** Multiplicar cada dígito binário pela potência de 2 correspondente à sua posição e somar os resultados.
    *   **Binário para Hexadecimal:** Agrupar os dígitos binários em conjuntos de 4 (da direita para a esquerda) e converter cada grupo para seu equivalente hexadecimal.
    *   **Hexadecimal para Binário:** Converter cada dígito hexadecimal para seu equivalente binário de 4 dígitos.
    *   **Decimal para Hexadecimal:** Dividir o número decimal sucessivamente por 16 e anotar os restos (usando A-F para 10-15) na ordem inversa.
    *   **Hexadecimal para Decimal:** Multiplicar cada dígito hexadecimal pela potência de 16 correspondente à sua posição e somar os resultados.

#### Sexta-feira: Representação de dados: bits, bytes, ASCII, Unicode. Unidades de medida (Kb, Mb, Gb, TB).

A forma como os dados são representados e medidos é fundamental para a computação:

*   **Bits e Bytes:**
    *   **Bit (Binary Digit):** É a menor unidade de informação em um computador, representando um 0 ou um 1. É a base de todo o processamento digital.
    *   **Byte:** É um grupo de 8 bits. Um byte é a unidade básica para armazenar um caractere (letra, número, símbolo) e é a unidade de medida mais comum para o tamanho de arquivos e memória.

*   **ASCII (American Standard Code for Information Interchange):** É um padrão de codificação de caracteres que atribui um número único a cada letra, número e símbolo. Originalmente, usava 7 bits para representar 128 caracteres (0 a 127), incluindo letras maiúsculas e minúsculas do alfabeto inglês, números e símbolos básicos. Foi um dos primeiros e mais influentes padrões de codificação.

*   **Unicode:** É um padrão de codificação de caracteres mais abrangente e moderno que visa representar todos os caracteres de todos os sistemas de escrita do mundo. Ele atribui um número único (code point) a cada caractere, independentemente da plataforma, programa ou idioma. O Unicode é implementado por diferentes codificações, sendo as mais comuns:
    *   **UTF-8:** A codificação mais utilizada na web, é compatível com ASCII e usa um número variável de bytes (1 a 4) para representar caracteres, tornando-o eficiente para textos em diferentes idiomas.
    *   **UTF-16:** Usa 2 ou 4 bytes por caractere.
    *   **UTF-32:** Usa 4 bytes por caractere.

*   **Unidades de Medida de Dados:** Para quantificar o volume de dados, utilizamos unidades baseadas em potências de 2 (embora frequentemente aproximadas para potências de 10 no marketing):
    *   **Kilobyte (KB):** 1 KB = 1024 bytes (aproximadamente mil bytes).
    *   **Megabyte (MB):** 1 MB = 1024 KB (aproximadamente um milhão de bytes).
    *   **Gigabyte (GB):** 1 GB = 1024 MB (aproximadamente um bilhão de bytes).
    *   **Terabyte (TB):** 1 TB = 1024 GB (aproximadamente um trilhão de bytes).
    *   Outras unidades maiores incluem Petabyte (PB), Exabyte (EB), Zettabyte (ZB) e Yottabyte (YB).

---
### Semana 3 – Lógica Matemática Aplicada à Computação

#### Segunda-feira: Lógica proposicional: proposições, conectivos lógicos (E, OU, NÃO, IMPLICA, BICONDICIONAL). Tabela-verdade.

A **Lógica Proposicional** é um ramo da lógica matemática que estuda as proposições e as relações entre elas. Uma **proposição** é uma sentença declarativa que pode ser classificada como verdadeira (V) ou falsa (F), mas nunca ambas simultaneamente. Exemplos de proposições são "O céu é azul" ou "2 + 2 = 5". Frases interrogativas, exclamativas ou imperativas não são proposições.

Para combinar e modificar proposições, utilizamos **conectivos lógicos**:

*   **NÃO (Negação - ¬ ou ~):** Inverte o valor lógico de uma proposição. Se P é verdadeira, ¬P é falsa; se P é falsa, ¬P é verdadeira.
*   **E (Conjunção - ∧):** A proposição composta (P ∧ Q) é verdadeira somente se ambas as proposições P e Q forem verdadeiras. Caso contrário, é falsa.
*   **OU (Disjunção - ∨):** A proposição composta (P ∨ Q) é verdadeira se pelo menos uma das proposições P ou Q for verdadeira. É falsa somente se ambas forem falsas.
*   **IMPLICA (Condicional - → ou ⇒):** A proposição composta (P → Q) é falsa somente se P for verdadeira e Q for falsa. Em todos os outros casos, é verdadeira. P é o antecedente e Q é o consequente.
*   **BICONDICIONAL (Se e Somente Se - ↔ ou ⇔):** A proposição composta (P ↔ Q) é verdadeira se P e Q tiverem o mesmo valor lógico (ambas verdadeiras ou ambas falsas). Caso contrário, é falsa.

A **Tabela-Verdade** é uma ferramenta fundamental na lógica proposicional que lista todos os possíveis valores lógicos de uma ou mais proposições e os valores lógicos resultantes das proposições compostas formadas por elas. Ela permite analisar a validade de argumentos e a equivalência entre expressões lógicas.

| P | Q | ¬P | P ∧ Q | P ∨ Q | P → Q | P ↔ Q |
|---|---|----|-------|-------|-------|-------|
| V | V | F  | V     | V     | V     | V     |
| V | F | F  | F     | V     | F     | F     |
| F | V | V  | F     | V     | V     | F     |
| F | F | V  | F     | F     | V     | V     |

#### Terça-feira: Equivalências lógicas (De Morgan, distributiva, associativa). Simplificação de expressões.

**Equivalências Lógicas** são relações entre proposições compostas que possuem o mesmo valor lógico para todas as possíveis atribuições de valores verdadeiros ou falsos às suas proposições simples. Conhecer essas equivalências é crucial para simplificar expressões lógicas e provar argumentos. Algumas das mais importantes são:

*   **Leis de De Morgan:**
    *   ¬(P ∧ Q) ≡ (¬P ∨ ¬Q) - A negação de uma conjunção é a disjunção das negações.
    *   ¬(P ∨ Q) ≡ (¬P ∧ ¬Q) - A negação de uma disjunção é a conjunção das negações.

*   **Leis Distributivas:**
    *   P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R) - A conjunção distribui-se sobre a disjunção.
    *   P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R) - A disjunção distribui-se sobre a conjunção.

*   **Leis Associativas:**
    *   (P ∧ Q) ∧ R ≡ P ∧ (Q ∧ R) - A ordem da conjunção não altera o resultado.
    *   (P ∨ Q) ∨ R ≡ P ∨ (Q ∨ R) - A ordem da disjunção não altera o resultado.

Outras equivalências importantes incluem as leis comutativas, de identidade, de dominância, de idempotência, de absorção e a dupla negação (¬(¬P) ≡ P).

A **Simplificação de Expressões Lógicas** envolve o uso dessas equivalências para transformar uma expressão complexa em uma forma mais simples, mas logicamente equivalente. Isso é fundamental em áreas como o design de circuitos digitais, onde a simplificação pode reduzir o número de componentes necessários, e na otimização de código em programação.

#### Quarta-feira: Álgebra booleana: postulados, portas lógicas (AND, OR, NOT, NAND, NOR, XOR). Construção de circuitos simples.

A **Álgebra Booleana**, desenvolvida por George Boole, é um sistema matemático que lida com valores lógicos (verdadeiro/falso, 1/0) e operações lógicas. É a base teórica para o funcionamento de todos os circuitos digitais e computadores. Seus **postulados** definem as propriedades das operações lógicas, como comutatividade, associatividade, distributividade, identidade e complemento.

As **Portas Lógicas** são os blocos construtivos fundamentais dos circuitos digitais. Elas implementam as operações da álgebra booleana e recebem uma ou mais entradas binárias (0 ou 1) para produzir uma única saída binária. As portas lógicas básicas são:

*   **AND (E):** A saída é 1 somente se todas as entradas forem 1.
*   **OR (OU):** A saída é 1 se pelo menos uma das entradas for 1.
*   **NOT (NÃO - Inversor):** A saída é o inverso da entrada (se a entrada é 1, a saída é 0; se a entrada é 0, a saída é 1).
*   **NAND (NÃO E):** É o inverso da porta AND. A saída é 0 somente se todas as entradas forem 1.
*   **NOR (NÃO OU):** É o inverso da porta OR. A saída é 1 somente se todas as entradas forem 0.
*   **XOR (OU Exclusivo):** A saída é 1 se as entradas forem diferentes. Se as entradas forem iguais, a saída é 0.

A **Construção de Circuitos Simples** envolve a combinação dessas portas lógicas para realizar funções mais complexas. Por exemplo, um somador binário, um multiplexador ou um decodificador podem ser construídos a partir de portas lógicas básicas. A representação desses circuitos é feita através de diagramas lógicos, onde cada porta é simbolizada por um ícone específico.

#### Quinta-feira: Lógica de predicados: quantificadores (∀, ∃). Aplicações em banco de dados e programação.

A **Lógica de Predicados** (ou Lógica de Primeira Ordem) é uma extensão da lógica proposicional que permite expressar sentenças mais complexas, lidando com objetos, propriedades e relações. Ela introduz o conceito de **predicados**, que são funções que retornam um valor booleano (verdadeiro ou falso) dependendo dos argumentos que recebem (ex: P(x) = "x é par").

Os **quantificadores** são símbolos que indicam a quantidade de elementos para os quais um predicado é verdadeiro:

*   **Quantificador Universal (∀ - "Para todo" ou "Para qualquer"):** Indica que uma propriedade é válida para todos os elementos de um determinado domínio. Ex: ∀x P(x) significa "Para todo x, P(x) é verdadeiro".
*   **Quantificador Existencial (∃ - "Existe" ou "Pelo menos um"):** Indica que existe pelo menos um elemento em um determinado domínio para o qual uma propriedade é verdadeira. Ex: ∃x P(x) significa "Existe um x tal que P(x) é verdadeiro".

**Aplicações em Banco de Dados:** A lógica de predicados é a base teórica para as linguagens de consulta a bancos de dados, como o SQL (Structured Query Language). As cláusulas `WHERE` e `HAVING` em SQL, por exemplo, utilizam predicados para filtrar registros que satisfazem certas condições. A teoria de conjuntos e a lógica de predicados são fundamentais para o modelo relacional de bancos de dados.

**Aplicações em Programação:** Em programação, a lógica de predicados é usada para expressar condições em estruturas de controle (if/else, loops), para validar entradas, para filtrar coleções de dados e para definir regras em sistemas baseados em conhecimento. Expressões regulares, por exemplo, podem ser vistas como uma forma de aplicar lógica de predicados para buscar padrões em textos.

#### Sexta-feira: Aplicações em computação: circuitos aritméticos (somador, flip-flop), autômatos finitos. Introdução à lógica difusa.

A lógica matemática tem diversas **aplicações práticas na computação**:

*   **Circuitos Aritméticos:** São circuitos digitais que realizam operações matemáticas básicas. Exemplos incluem:
    *   **Somador (Adder):** Um circuito que realiza a adição de números binários. Existem somadores de meio-bit (half-adder) e somadores completos (full-adder), que podem ser combinados para somar números de múltiplos bits.
    *   **Flip-Flop:** É um circuito sequencial fundamental que armazena um bit de informação. Ele tem dois estados estáveis (0 ou 1) e pode ser usado para construir registradores, contadores e memórias. Os tipos comuns incluem SR, JK, D e T flip-flops.

*   **Autômatos Finitos (Finite Automata - FA):** São modelos matemáticos abstratos de máquinas que podem estar em um número finito de estados. Eles são usados para modelar sistemas que têm um comportamento discreto e podem ser aplicados em:
    *   **Análise Léxica de Compiladores:** Para reconhecer palavras-chave, identificadores e operadores em um código-fonte.
    *   **Design de Protocolos de Comunicação:** Para garantir que as mensagens sejam trocadas na ordem correta.
    *   **Modelagem de Sistemas de Controle:** Para descrever o comportamento de máquinas de estado.

*   **Introdução à Lógica Difusa (Fuzzy Logic):** Diferente da lógica booleana, que lida apenas com verdadeiro ou falso (0 ou 1), a lógica difusa permite que os valores de verdade sejam graus de verdade entre 0 e 1. Isso a torna adequada para lidar com conceitos imprecisos ou vagos, como "quente", "frio", "alto" ou "baixo".
    *   **Aplicações:** Controle de sistemas (máquinas de lavar, ar condicionado, câmeras), reconhecimento de padrões, inteligência artificial e sistemas de apoio à decisão, onde a tomada de decisão humana muitas vezes envolve nuances e incertezas.

---
### Semana 4 – Redes de Computadores (básico → avançado)

#### Segunda-feira: Conceitos fundamentais: LAN, WAN, MAN. Topologias (estrela, anel, barramento). Meios guiados e não guiados.

As **redes de computadores** são sistemas que permitem a comunicação e o compartilhamento de recursos entre dispositivos. Para entender seu funcionamento, é crucial conhecer os conceitos fundamentais:

*   **Tipos de Redes por Abrangência Geográfica:**
    *   **LAN (Local Area Network - Rede Local):** Abrange uma área geográfica limitada, como uma casa, escritório ou campus. Caracteriza-se por altas velocidades de transmissão e baixa latência. Exemplos incluem redes Wi-Fi domésticas ou redes Ethernet em um prédio.
    *   **WAN (Wide Area Network - Rede de Longa Distância):** Abrange grandes áreas geográficas, conectando LANs em diferentes cidades, estados ou países. A internet é o maior exemplo de WAN. Geralmente envolve velocidades mais baixas e maior latência em comparação com as LANs.
    *   **MAN (Metropolitan Area Network - Rede Metropolitana):** Abrange uma área geográfica de uma cidade ou região metropolitana. Conecta várias LANs dentro de uma cidade e geralmente é operada por uma única organização ou provedor de serviços.

*   **Topologias de Rede:** Descrevem a forma como os dispositivos estão fisicamente ou logicamente conectados em uma rede:
    *   **Estrela:** Todos os dispositivos se conectam a um ponto central (hub ou switch). É a topologia mais comum atualmente. Se o ponto central falhar, toda a rede para. Fácil de instalar e gerenciar.
    *   **Anel:** Os dispositivos são conectados em um loop fechado, onde cada dispositivo se conecta a exatamente dois vizinhos. Os dados viajam em uma direção. A falha de um único dispositivo pode interromper a comunicação em toda a rede.
    *   **Barramento:** Todos os dispositivos se conectam a um único cabo principal (barramento). É uma topologia simples e barata, mas a falha no cabo principal interrompe a rede e é difícil de diagnosticar problemas.

*   **Meios de Transmissão:** São os canais físicos ou sem fio pelos quais os dados são transmitidos:
    *   **Meios Guiados (com fio):**
        *   **Cabo Par Trançado (UTP/STP):** Mais comum em LANs Ethernet. Os fios são trançados para reduzir interferências. Categoria 5e, 6, 6a, 7, 8.
        *   **Cabo Coaxial:** Usado em redes mais antigas e em TV a cabo. Possui um condutor central e uma malha de blindagem.
        *   **Fibra Óptica:** Transmite dados usando pulsos de luz. Oferece altíssimas velocidades, grande largura de banda e imunidade a interferências eletromagnéticas. Ideal para longas distâncias e backbones de rede.
    *   **Meios Não Guiados (sem fio):**
        *   **Ondas de Rádio:** Usadas em redes Wi-Fi, Bluetooth, redes celulares. A transmissão ocorre pelo ar.
        *   **Micro-ondas:** Usadas para links de longa distância, como em redes de satélite ou enlaces ponto a ponto.
        *   **Infravermelho:** Usado para comunicação de curto alcance, como em controles remotos.

#### Terça-feira: Modelo OSI e TCP/IP: camadas, encapsulamento, PDU. Principais protocolos (IP, TCP, UDP, HTTP, DNS).

Para padronizar e organizar a comunicação em redes, foram desenvolvidos modelos de referência:

*   **Modelo OSI (Open Systems Interconnection - Interconexão de Sistemas Abertos):** É um modelo conceitual de 7 camadas que descreve como os dados devem ser transmitidos entre diferentes sistemas. Cada camada tem uma função específica e se comunica apenas com as camadas adjacentes. As camadas são:
    1.  **Física:** Transmissão de bits brutos pelo meio físico (cabos, ondas de rádio).
    2.  **Enlace:** Controle de acesso ao meio, detecção e correção de erros no nível do hardware (endereçamento MAC).
    3.  **Rede:** Endereçamento lógico (IP), roteamento de pacotes entre redes.
    4.  **Transporte:** Segmentação de dados, controle de fluxo, confiabilidade da entrega (TCP, UDP).
    5.  **Sessão:** Gerenciamento de sessões de comunicação entre aplicações.
    6.  **Apresentação:** Formatação e codificação de dados, criptografia.
    7.  **Aplicação:** Interface para os aplicativos de rede (HTTP, FTP, SMTP).

*   **Modelo TCP/IP (Transmission Control Protocol/Internet Protocol):** É o modelo de referência e o conjunto de protocolos mais utilizado na internet. É mais prático e possui 4 camadas (às vezes 5, dependendo da interpretação):
    1.  **Acesso à Rede (ou Enlace):** Combina as camadas Física e de Enlace do OSI.
    2.  **Internet (ou Rede):** Corresponde à camada de Rede do OSI (IP).
    3.  **Transporte:** Corresponde à camada de Transporte do OSI (TCP, UDP).
    4.  **Aplicação:** Combina as camadas de Sessão, Apresentação e Aplicação do OSI (HTTP, DNS, FTP).

*   **Encapsulamento:** É o processo pelo qual os dados de uma camada superior são envolvidos com informações de controle (cabeçalhos) da camada atual, formando uma **PDU (Protocol Data Unit - Unidade de Dados de Protocolo)**. Essa PDU é então passada para a camada inferior, que adiciona seu próprio cabeçalho, e assim por diante, até a camada física. Na recepção, o processo é inverso (desencapsulamento).

*   **Principais Protocolos:**
    *   **IP (Internet Protocol):** Responsável pelo endereçamento lógico e roteamento de pacotes na internet. Define como os dados são enviados de um host para outro.
    *   **TCP (Transmission Control Protocol):** Protocolo da camada de transporte que oferece comunicação confiável, orientada à conexão, com controle de fluxo e retransmissão de pacotes perdidos. Usado por aplicações que exigem alta confiabilidade (ex: HTTP, FTP).
    *   **UDP (User Datagram Protocol):** Protocolo da camada de transporte que oferece comunicação não confiável, sem conexão, mais rápido que o TCP, mas sem garantia de entrega ou controle de fluxo. Usado por aplicações que priorizam velocidade (ex: streaming de vídeo, jogos online, DNS).
    *   **HTTP (Hypertext Transfer Protocol):** Protocolo da camada de aplicação usado para a comunicação na World Wide Web, para transferir páginas HTML, imagens e outros recursos.
    *   **DNS (Domain Name System):** Sistema que traduz nomes de domínio legíveis por humanos (ex: www.google.com) em endereços IP numéricos que os computadores usam para se comunicar.

#### Quarta-feira: Endereçamento IP: IPv4 (classes, sub-redes, CIDR), IPv6. Máscara de rede, gateway, broadcast.

O **endereçamento IP** é fundamental para identificar dispositivos em uma rede e permitir que eles se comuniquem. Existem duas versões principais:

*   **IPv4 (Internet Protocol version 4):** É a versão mais antiga e ainda amplamente utilizada. Os endereços IPv4 são números de 32 bits, geralmente representados em notação decimal pontuada (ex: 192.168.1.1). Devido ao esgotamento dos endereços, técnicas como NAT (Network Address Translation) e CIDR foram desenvolvidas.
    *   **Classes de Endereços (A, B, C):** Historicamente, os endereços IPv4 eram divididos em classes, que determinavam o tamanho da porção de rede e de host do endereço. Essa divisão é menos relevante hoje com o CIDR.
        *   **Classe A:** Grandes redes (primeiro octeto de 1 a 126).
        *   **Classe B:** Redes de médio porte (primeiro octeto de 128 a 191).
        *   **Classe C:** Pequenas redes (primeiro octeto de 192 a 223).
    *   **Sub-redes (Subnetting):** Permite dividir uma rede maior em redes menores (sub-redes), otimizando o uso de endereços IP e melhorando a segurança e o desempenho da rede.
    *   **CIDR (Classless Inter-Domain Routing - Roteamento Entre Domínios Sem Classes):** Substituiu o sistema de classes. Permite uma alocação mais flexível de endereços IP usando uma notação de prefixo (ex: 192.168.1.0/24), onde o número após a barra indica a quantidade de bits da porção de rede.

*   **IPv6 (Internet Protocol version 6):** É a versão mais recente do protocolo IP, desenvolvida para substituir o IPv4 e resolver o problema do esgotamento de endereços. Os endereços IPv6 são números de 128 bits, representados em notação hexadecimal (ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334). Oferece um espaço de endereçamento vastíssimo e recursos aprimorados de segurança e autoconfiguração.

*   **Máscara de Rede (Subnet Mask):** É um número de 32 bits (para IPv4) que, em conjunto com o endereço IP, define qual parte do endereço IP identifica a rede e qual parte identifica o host dentro dessa rede. Ela é usada para determinar se um endereço IP está na mesma rede local ou em uma rede remota.

*   **Gateway (Gateway Padrão):** É o endereço IP do dispositivo (geralmente um roteador) que atua como ponto de saída da rede local para outras redes (como a internet). Todos os pacotes destinados a endereços fora da rede local são enviados para o gateway.

*   **Endereço de Broadcast:** É um endereço especial usado para enviar dados para todos os dispositivos em uma determinada rede ou sub-rede. No IPv4, o endereço de broadcast é o último endereço de uma sub-rede (todos os bits de host são 1).

#### Quinta-feira: Roteamento e switching: tabela de roteamento, protocolos RIP, OSPF. VLAN, NAT, DHCP.

**Roteamento e Switching** são processos fundamentais para a comunicação em redes, especialmente em redes complexas e na internet:

*   **Roteamento:** É o processo de selecionar o melhor caminho para os pacotes de dados viajarem de uma rede de origem para uma rede de destino. Os dispositivos que realizam o roteamento são os **roteadores**.
    *   **Tabela de Roteamento:** Cada roteador mantém uma tabela que contém informações sobre as redes que ele conhece, os próximos saltos (next hop) para alcançar essas redes e a métrica (custo) associada a cada caminho. Essa tabela é usada para decidir para onde encaminhar um pacote.
    *   **Protocolos de Roteamento:** São algoritmos que os roteadores usam para trocar informações sobre as redes e construir suas tabelas de roteamento:
        *   **RIP (Routing Information Protocol):** Um protocolo de roteamento de vetor de distância mais antigo e simples. Usa contagem de saltos (hops) como métrica e é adequado para redes pequenas.
        *   **OSPF (Open Shortest Path First):** Um protocolo de roteamento de estado de link mais moderno e complexo. Constrói um mapa completo da topologia da rede e usa o algoritmo de Dijkstra para calcular o caminho mais curto. Adequado para redes grandes e complexas.

*   **Switching:** É o processo de encaminhar quadros de dados dentro de uma mesma rede local (LAN). Os dispositivos que realizam o switching são os **switches**.
    *   Um switch aprende os endereços MAC dos dispositivos conectados às suas portas e cria uma tabela de endereços MAC para encaminhar os quadros diretamente para a porta correta, em vez de inundar todas as portas como um hub.

*   **VLAN (Virtual Local Area Network - Rede Local Virtual):** Permite dividir uma única rede física em múltiplas redes lógicas (VLANs). Dispositivos em VLANs diferentes não podem se comunicar diretamente, mesmo que estejam conectados ao mesmo switch físico, a menos que um roteador ou switch de camada 3 seja usado para rotear o tráfego entre elas. VLANs melhoram a segurança, o desempenho e a organização da rede.

*   **NAT (Network Address Translation - Tradução de Endereços de Rede):** É uma técnica usada para traduzir endereços IP privados (usados internamente em uma rede local) em um único endereço IP público (usado na internet). Isso permite que múltiplos dispositivos em uma LAN compartilhem um único endereço IP público, economizando endereços IPv4 e adicionando uma camada de segurança.

*   **DHCP (Dynamic Host Configuration Protocol):** É um protocolo que atribui automaticamente endereços IP e outras configurações de rede (máscara de rede, gateway, DNS) aos dispositivos em uma rede. Isso simplifica a administração da rede, eliminando a necessidade de configurar manualmente cada dispositivo.

#### Sexta-feira: Segurança e avançado: firewalls, VPN, IDS/IPS. Redes definidas por software (SDN). Análise de tráfego com Wireshark.

A **segurança de redes** é uma preocupação crescente, e diversas ferramentas e conceitos avançados são utilizados para proteger os dados e a infraestrutura:

*   **Firewalls:** São sistemas de segurança que monitoram e controlam o tráfego de rede de entrada e saída com base em regras de segurança predefinidas. Eles atuam como uma barreira entre uma rede confiável (interna) e uma rede não confiável (externa, como a internet), bloqueando acessos não autorizados e protegendo contra ameaças.

*   **VPN (Virtual Private Network - Rede Privada Virtual):** Cria uma conexão segura e criptografada sobre uma rede pública (como a internet). Isso permite que usuários remotos acessem recursos de uma rede privada como se estivessem fisicamente conectados a ela, garantindo privacidade e segurança dos dados transmitidos.

*   **IDS/IPS (Intrusion Detection System / Intrusion Prevention System):**
    *   **IDS (Sistema de Detecção de Intrusão):** Monitora o tráfego de rede em busca de atividades maliciosas ou violações de políticas de segurança. Ele alerta os administradores sobre possíveis ataques, mas não os impede ativamente.
    *   **IPS (Sistema de Prevenção de Intrusão):** Além de detectar, também toma ações para bloquear ou impedir ataques em tempo real, como descartar pacotes maliciosos ou reconfigurar firewalls.

*   **Redes Definidas por Software (SDN - Software-Defined Networking):** É uma abordagem para gerenciar redes que separa o plano de controle (que decide como o tráfego deve ser encaminhado) do plano de dados (que encaminha o tráfego). Isso permite que os administradores de rede gerenciem e configurem a rede de forma centralizada e programática, usando software, em vez de configurar individualmente cada dispositivo de rede. SDN oferece maior flexibilidade, agilidade e automação.

*   **Análise de Tráfego com Wireshark:** O Wireshark é uma ferramenta de código aberto amplamente utilizada para **análise de tráfego de rede (packet sniffing)**. Ele captura e exibe pacotes de dados que trafegam por uma rede, permitindo que os administradores e analistas de segurança inspecionem o conteúdo dos pacotes, identifiquem problemas de rede, depurem protocolos e detectem atividades suspeitas ou maliciosas. É uma ferramenta essencial para diagnóstico e segurança de redes.

---
### Semana 5 – Sistemas Operacionais I (básico → avançado)

#### Segunda-feira: Conceitos iniciais: o que é um SO, funções (gerenciamento de processos, memória, arquivos). Tipos: batch, tempo real, multiusuário.

Um **Sistema Operacional (SO)** é o software mais importante que roda em um computador. Ele gerencia o hardware e o software do computador, fornecendo serviços comuns para programas de computador e gerenciando a alocação de recursos. Sem um SO, o computador seria apenas um conjunto de peças sem utilidade.

**Funções Principais de um SO:**

*   **Gerenciamento de Processos:** O SO é responsável por criar, agendar, executar e finalizar processos (programas em execução). Ele aloca recursos do CPU para cada processo, garantindo que eles funcionem de forma eficiente e sem interferir uns nos outros.
*   **Gerenciamento de Memória:** O SO controla como a memória RAM é alocada e desalocada para os programas. Ele garante que cada programa tenha acesso à memória de que precisa e que um programa não acesse a memória de outro, protegendo a integridade do sistema.
*   **Gerenciamento de Arquivos:** O SO organiza e gerencia os arquivos e diretórios em dispositivos de armazenamento (HDDs, SSDs). Ele fornece uma estrutura para armazenar, recuperar, criar, copiar, mover e excluir arquivos, além de controlar as permissões de acesso.
*   **Gerenciamento de Dispositivos (E/S):** O SO gerencia a comunicação entre o CPU e os dispositivos de entrada/saída (teclado, mouse, impressora, monitor, etc.), traduzindo as solicitações dos programas para os comandos que o hardware entende.
*   **Interface com o Usuário:** Fornece uma maneira para o usuário interagir com o computador, seja através de uma interface gráfica (GUI) ou de linha de comando (CLI).

**Tipos de Sistemas Operacionais:**

*   **Sistemas Batch (em Lotes):** Os primeiros SOs, projetados para executar tarefas em lotes, sem interação direta do usuário durante a execução. As tarefas eram agrupadas e processadas sequencialmente. Não são mais comuns em computadores pessoais, mas ainda usados em grandes sistemas para processamento de dados.
*   **Sistemas de Tempo Real (Real-Time Operating Systems - RTOS):** Projetados para garantir que as operações sejam concluídas dentro de prazos rigorosos e previsíveis. São usados em sistemas críticos onde o tempo de resposta é crucial, como controle industrial, sistemas embarcados, equipamentos médicos e automação automotiva.
*   **Sistemas Multiusuário:** Permitem que múltiplos usuários acessem e utilizem o mesmo computador simultaneamente, cada um com seu próprio ambiente e recursos. Exemplos incluem servidores Linux e sistemas de mainframe.
*   **Sistemas Monousuário:** Projetados para serem usados por um único usuário por vez, embora possam executar múltiplas tarefas. Exemplos incluem Windows e macOS em computadores pessoais.

#### Terça-feira: Gerenciamento de processos: PCB, estados (novo, pronto, execução, bloqueado, terminado). Escalonamento (FCFS, SJF, Round Robin, prioridade).

O **gerenciamento de processos** é uma das funções mais críticas de um sistema operacional, garantindo que os programas sejam executados de forma eficiente e justa.

*   **Process Control Block (PCB - Bloco de Controle de Processo):** É uma estrutura de dados mantida pelo SO para cada processo. O PCB contém informações essenciais sobre o processo, como:
    *   ID do processo (PID)
    *   Estado do processo (novo, pronto, execução, bloqueado, terminado)
    *   Contador de programa (endereço da próxima instrução a ser executada)
    *   Registradores do CPU
    *   Informações de agendamento do CPU (prioridade, tempo de execução)
    *   Informações de gerenciamento de memória
    *   Informações de contabilidade (tempo de CPU usado, tempo real)
    *   Informações de E/S (arquivos abertos, dispositivos alocados)

*   **Estados de um Processo:** Um processo passa por diferentes estados durante sua vida útil:
    *   **Novo (New):** O processo está sendo criado.
    *   **Pronto (Ready):** O processo está esperando para ser alocado ao CPU.
    *   **Execução (Running):** O processo está sendo executado pelo CPU.
    *   **Bloqueado (Waiting/Blocked):** O processo está esperando por algum evento (ex: conclusão de E/S, recebimento de um sinal).
    *   **Terminado (Terminated):** O processo concluiu sua execução.

*   **Escalonamento de Processos (CPU Scheduling):** É a atividade de decidir qual processo na fila de prontos deve ser executado pelo CPU. O objetivo é otimizar o uso do CPU, minimizar o tempo de resposta e garantir a justiça. Alguns algoritmos de escalonamento comuns incluem:
    *   **FCFS (First-Come, First-Served - Primeiro a Chegar, Primeiro a Ser Servido):** Os processos são executados na ordem em que chegam à fila de prontos. Simples, mas pode levar a um tempo de espera longo para processos curtos se um processo longo chegar primeiro.
    *   **SJF (Shortest Job First - Menor Trabalho Primeiro):** O processo com o menor tempo de execução estimado é executado primeiro. Ideal em termos de tempo médio de espera, mas difícil de implementar na prática, pois o tempo de execução futuro é desconhecido.
    *   **Round Robin:** Cada processo recebe uma fatia de tempo (quantum) para executar. Se o processo não terminar dentro do quantum, ele é preemptado e colocado de volta no final da fila de prontos. Garante que todos os processos recebam tempo de CPU, bom para sistemas interativos.
    *   **Prioridade:** Cada processo recebe um número de prioridade. O CPU é alocado ao processo com a maior prioridade. Pode levar à inanição (starvation) de processos de baixa prioridade se processos de alta prioridade continuarem chegando.

#### Quarta-feira: Threads e concorrência: diferença entre processo e thread, problemas de condições de corrida, semáforos, mutexes. Deadlock (condições e prevenção).

A **concorrência** é a capacidade de um sistema lidar com múltiplas tarefas que progridem simultaneamente. **Processos e threads** são as unidades básicas de concorrência:

*   **Diferença entre Processo e Thread:**
    *   **Processo:** É uma instância de um programa em execução. Cada processo tem seu próprio espaço de endereço de memória, recursos (arquivos abertos, variáveis globais) e PCB. A comunicação entre processos é mais complexa (IPC - Interprocess Communication).
    *   **Thread (Linha de Execução):** É uma unidade de execução dentro de um processo. Threads de um mesmo processo compartilham o mesmo espaço de endereço de memória e recursos, mas cada thread tem seu próprio contador de programa, pilha e registradores. A comunicação entre threads é mais fácil e eficiente. Threads são mais leves para criar e gerenciar do que processos.

*   **Problemas de Condições de Corrida (Race Conditions):** Ocorrem quando múltiplas threads ou processos acessam e manipulam dados compartilhados simultaneamente, e o resultado final depende da ordem particular em que as operações são executadas. Isso pode levar a resultados inconsistentes e erros difíceis de depurar.

*   **Mecanismos de Sincronização (para evitar condições de corrida):**
    *   **Seção Crítica:** Uma parte do código onde os recursos compartilhados são acessados. Apenas uma thread/processo deve estar na seção crítica por vez.
    *   **Semáforos:** São variáveis inteiras (ou abstratas) usadas para controlar o acesso a recursos compartilhados. Um semáforo binário (0 ou 1) pode ser usado como um *mutex*. Um semáforo contador pode controlar o acesso a um número limitado de recursos.
    *   **Mutexes (Mutual Exclusion - Exclusão Mútua):** São mecanismos de bloqueio que garantem que apenas uma thread/processo possa acessar uma seção crítica por vez. Uma thread adquire o mutex antes de entrar na seção crítica e o libera ao sair.
    *   **Monitores:** Estruturas de alto nível que encapsulam dados compartilhados e os procedimentos que operam sobre esses dados, garantindo exclusão mútua.

*   **Deadlock (Impasse):** É uma situação em que dois ou mais processos/threads ficam bloqueados indefinidamente, esperando por um recurso que está sendo mantido por outro processo/thread que também está esperando por um recurso. As quatro condições necessárias para um deadlock ocorrer são:
    1.  **Exclusão Mútua:** Pelo menos um recurso deve ser não compartilhável (apenas um processo por vez pode usá-lo).
    2.  **Posse e Espera (Hold and Wait):** Um processo deve estar segurando pelo menos um recurso e esperando para adquirir recursos adicionais que estão sendo segurados por outros processos.
    3.  **Não Preempção:** Os recursos não podem ser preemptados; eles só podem ser liberados voluntariamente pelo processo que os está segurando.
    4.  **Espera Circular (Circular Wait):** Deve existir uma cadeia de processos P1, P2, ..., Pn tal que P1 está esperando por um recurso de P2, P2 por P3, ..., e Pn por P1.

*   **Prevenção de Deadlock:** Abordagens para evitar deadlock incluem:
    *   **Prevenção:** Eliminar uma ou mais das quatro condições necessárias para o deadlock.
    *   **Evitação:** O SO aloca recursos de forma que o sistema nunca entre em um estado inseguro (ex: Algoritmo do Banqueiro).
    *   **Detecção e Recuperação:** Permitir que o deadlock ocorra, detectá-lo e então recuperá-lo (ex: terminar um processo, preemptar recursos).

#### Quinta-feira: Gerenciamento de memória: alocação contígua, paginação, segmentação, memória virtual (TLB, page fault). Thrashing.

O **gerenciamento de memória** é a função do sistema operacional que lida com a memória principal, alocando e desalocando espaço para os programas e garantindo que eles não interfiram uns nos outros.

*   **Alocação Contígua:** É a forma mais simples de alocação de memória, onde cada processo recebe um bloco contíguo de memória. Isso pode levar à fragmentação externa (espaços livres pequenos demais para serem usados) e exige que o processo seja carregado completamente na memória.

*   **Paginação:** É uma técnica de gerenciamento de memória não contígua que divide a memória física em blocos de tamanho fixo chamados **frames** e a memória lógica (espaço de endereço do processo) em blocos de mesmo tamanho chamados **páginas**. Quando um processo é carregado, suas páginas podem ser espalhadas por frames não contíguos na memória física. Uma **tabela de páginas** mapeia as páginas lógicas para os frames físicos.
    *   **Vantagens:** Elimina a fragmentação externa, permite que programas maiores que a memória física sejam executados.

*   **Segmentação:** É outra técnica de gerenciamento de memória não contígua que divide a memória lógica em segmentos de tamanho variável, que correspondem a unidades lógicas do programa (ex: código, dados, pilha). Cada segmento pode ser carregado em qualquer lugar da memória física. Uma **tabela de segmentos** mapeia os segmentos lógicos para a memória física.
    *   **Vantagens:** Facilita a proteção e o compartilhamento de código e dados.

*   **Memória Virtual:** É uma técnica que permite que um programa use mais memória do que a fisicamente disponível. Ela combina a RAM com espaço em disco (arquivo de paginação ou swap file) para criar um espaço de endereço virtual maior. O SO gerencia a movimentação de páginas entre a RAM e o disco.
    *   **TLB (Translation Lookaside Buffer):** É um cache de hardware pequeno e rápido que armazena as traduções mais recentes de endereços virtuais para físicos. Acelera o processo de tradução de endereços, pois evita a consulta à tabela de páginas na memória principal na maioria das vezes.
    *   **Page Fault (Falha de Página):** Ocorre quando um programa tenta acessar uma página que não está atualmente na memória RAM. O SO então precisa carregar essa página do disco para a RAM, o que é uma operação lenta.

*   **Thrashing:** É uma condição em que o sistema gasta a maior parte do seu tempo movendo páginas entre a RAM e o disco (devido a page faults frequentes) em vez de executar instruções úteis. Isso acontece quando há muitos processos competindo por pouca memória RAM, resultando em uma degradação severa do desempenho do sistema.

#### Sexta-feira: Sistemas de arquivos: FAT32, NTFS, ext4, inode, journaling. Permissões (Unix x Windows). Introdução a sistemas de arquivos distribuídos.

Os **sistemas de arquivos** são a forma como o sistema operacional organiza e gerencia os arquivos e diretórios em um dispositivo de armazenamento. Eles definem como os dados são armazenados, acessados e protegidos.

*   **Tipos de Sistemas de Arquivos:**
    *   **FAT32 (File Allocation Table 32):** Um sistema de arquivos mais antigo, amplamente compatível, mas com limitações de tamanho de arquivo (máximo de 4 GB) e tamanho de partição. Não oferece recursos avançados de segurança ou recuperação.
    *   **NTFS (New Technology File System):** O sistema de arquivos padrão do Windows. Oferece recursos avançados como segurança (permissões de arquivo e diretório), journaling, compressão, criptografia e suporte a arquivos e partições muito grandes. Mais robusto e confiável que o FAT32.
    *   **ext4 (Fourth Extended Filesystem):** O sistema de arquivos padrão para muitas distribuições Linux. Oferece bom desempenho, journaling, suporte a arquivos grandes e recursos de recuperação de dados. É uma evolução do ext3 e ext2.

*   **Inode (Index Node):** Em sistemas de arquivos Unix/Linux (como ext4), um inode é uma estrutura de dados que armazena metadados sobre um arquivo ou diretório, como permissões, proprietário, grupo, carimbos de data/hora, tamanho e ponteiros para os blocos de dados no disco. Cada arquivo e diretório tem um inode único.

*   **Journaling (Registro em Diário):** É um recurso de sistemas de arquivos modernos (NTFS, ext4) que registra as alterações que serão feitas no sistema de arquivos em um diário (journal) antes de realmente aplicá-las. Em caso de falha do sistema (ex: queda de energia), o sistema de arquivos pode ser rapidamente recuperado para um estado consistente, evitando a perda de dados e a necessidade de verificações demoradas.

*   **Permissões de Arquivo:**
    *   **Sistemas Unix/Linux:** As permissões são baseadas em três categorias de usuários (proprietário, grupo, outros) e três tipos de acesso (leitura, escrita, execução). São representadas por caracteres (rwx) ou números octais (ex: 755).
    *   **Sistemas Windows (NTFS):** As permissões são mais granulares e baseadas em Listas de Controle de Acesso (ACLs), que permitem definir permissões específicas para usuários e grupos em arquivos e diretórios, incluindo herança de permissões.

*   **Sistemas de Arquivos Distribuídos:** São sistemas que permitem que arquivos sejam armazenados em múltiplos servidores em uma rede e acessados como se estivessem em um único local. Oferecem alta disponibilidade, escalabilidade e tolerância a falhas. Exemplos incluem NFS (Network File System), SMB/CIFS (Server Message Block/Common Internet File System) e sistemas de arquivos em nuvem como HDFS (Hadoop Distributed File System).

---
### Semana 6 – Software Aplicativos + Tópicos Especiais para Informática

#### Segunda-feira: Software aplicativos: editores de texto (MS Word, Google Docs – formatação, estilos, mala direta). Planilhas (Excel: fórmulas, funções, tabela dinâmica).

**Software aplicativos** são programas projetados para realizar tarefas específicas para o usuário final. Eles contrastam com o software de sistema (como o sistema operacional), que gerencia o hardware do computador. Os aplicativos de produtividade são amplamente utilizados em ambientes pessoais e profissionais:

*   **Editores de Texto:** Ferramentas para criar, editar e formatar documentos de texto. Os mais populares incluem:
    *   **Microsoft Word:** Parte do pacote Microsoft Office, oferece recursos avançados de formatação, como estilos (para aplicar conjuntos de formatação consistentes), modelos, sumários automáticos e controle de alterações. A **mala direta** é uma funcionalidade poderosa que permite gerar cartas, envelopes ou etiquetas personalizadas para múltiplos destinatários a partir de uma lista de dados.
    *   **Google Docs:** Um editor de texto baseado em nuvem, parte do Google Workspace. Permite colaboração em tempo real, acesso de qualquer lugar e salvamento automático. Possui recursos de formatação e estilos, embora possa ser menos robusto que o Word em funcionalidades muito específicas.

*   **Planilhas Eletrônicas:** Ferramentas para organizar, analisar e manipular dados em formato de tabela. Os principais são:
    *   **Microsoft Excel:** O padrão da indústria para planilhas. Permite a criação de **fórmulas** (expressões matemáticas para calcular valores), **funções** (fórmulas pré-definidas para tarefas específicas, como SOMA, MÉDIA, SE) e **tabelas dinâmicas** (ferramentas poderosas para resumir, analisar, explorar e apresentar dados de forma interativa, permitindo a identificação de padrões e tendências).
    *   **Google Sheets:** A alternativa baseada em nuvem do Google para planilhas. Oferece colaboração em tempo real e uma vasta gama de fórmulas e funções, além de integração com outras ferramentas Google.

#### Terça-feira: Planilhas avançadas: macros, VBA, Power Query. Apresentações (PowerPoint: design, transições, animações). Suítes de escritório online.

Continuando com as ferramentas de produtividade, exploramos recursos mais avançados e outras categorias de aplicativos:

*   **Planilhas Avançadas (Excel):**
    *   **Macros:** Sequências de comandos e ações gravadas que podem ser executadas automaticamente para automatizar tarefas repetitivas. São criadas usando a funcionalidade de gravação de macro ou programadas diretamente.
    *   **VBA (Visual Basic for Applications):** É a linguagem de programação por trás das macros do Excel (e de outros aplicativos Office). Permite criar funcionalidades personalizadas, automatizar processos complexos e interagir com outros aplicativos.
    *   **Power Query:** Uma ferramenta de ETL (Extract, Transform, Load) integrada ao Excel que permite importar dados de diversas fontes (bancos de dados, arquivos, web), transformá-los (limpar, filtrar, combinar) e carregá-los na planilha para análise. Facilita a preparação de dados para relatórios e tabelas dinâmicas.

*   **Apresentações:** Ferramentas para criar slides visuais que acompanham uma fala ou palestra. O mais conhecido é:
    *   **Microsoft PowerPoint:** Permite criar apresentações com **design** profissional, utilizando modelos, layouts e temas. Oferece **transições** (efeitos visuais entre slides) e **animações** (efeitos visuais em objetos dentro de um slide) para tornar a apresentação mais dinâmica e envolvente.
    *   **Google Slides / Keynote (Apple):** Alternativas ao PowerPoint, com funcionalidades semelhantes e, no caso do Google Slides, forte foco na colaboração em nuvem.

*   **Suítes de Escritório Online:** Conjuntos de aplicativos de produtividade baseados em nuvem que oferecem funcionalidades de edição de texto, planilhas e apresentações diretamente no navegador. Exemplos incluem Google Workspace (Docs, Sheets, Slides) e Microsoft 365 Online (Word Online, Excel Online, PowerPoint Online). A principal vantagem é a colaboração em tempo real, o acesso de qualquer dispositivo e o salvamento automático.

#### Quarta-feira: Tópicos especiais: computação em nuvem (IaaS, PaaS, SaaS), exemplos AWS, Azure, Google Cloud.

A **computação em nuvem (Cloud Computing)** revolucionou a forma como a infraestrutura de TI é fornecida e consumida. Em vez de possuir e manter servidores e data centers físicos, as empresas podem alugar recursos computacionais (servidores, armazenamento, bancos de dados, software) de provedores de nuvem pela internet. Os principais modelos de serviço são:

*   **IaaS (Infrastructure as a Service - Infraestrutura como Serviço):** O provedor de nuvem oferece a infraestrutura básica de TI, como máquinas virtuais, armazenamento, redes e sistemas operacionais. O usuário tem controle total sobre o sistema operacional e os aplicativos, mas é responsável por gerenciá-los. É como alugar um terreno e construir sua própria casa. Ex: Amazon EC2, Azure Virtual Machines, Google Compute Engine.

*   **PaaS (Platform as a Service - Plataforma como Serviço):** O provedor de nuvem oferece uma plataforma completa para desenvolvimento, execução e gerenciamento de aplicativos, incluindo sistema operacional, ambiente de execução, banco de dados e ferramentas de desenvolvimento. O usuário se concentra apenas no código do aplicativo, sem se preocupar com a infraestrutura subjacente. É como alugar um apartamento mobiliado. Ex: AWS Elastic Beanstalk, Azure App Service, Google App Engine.

*   **SaaS (Software as a Service - Software como Serviço):** O provedor de nuvem hospeda e gerencia o aplicativo completo, que é disponibilizado aos usuários finais pela internet, geralmente por meio de um navegador web. O usuário não precisa se preocupar com a infraestrutura, o sistema operacional ou o desenvolvimento do aplicativo; ele apenas o utiliza. É como alugar um quarto de hotel. Ex: Gmail, Salesforce, Dropbox, Microsoft 365.

**Exemplos de Provedores de Nuvem:**
*   **AWS (Amazon Web Services):** O maior provedor de nuvem do mundo, com uma vasta gama de serviços.
*   **Microsoft Azure:** A plataforma de nuvem da Microsoft, com forte integração com produtos Microsoft.
*   **Google Cloud Platform (GCP):** A oferta de nuvem do Google, conhecida por seus serviços de dados e inteligência artificial.

#### Quinta-feira: IoT (Internet das Coisas): arquitetura, sensores, protocolos (MQTT, CoAP), plataformas (Arduino, Raspberry Pi). Edge computing.

A **IoT (Internet das Coisas)** refere-se à rede de objetos físicos ("coisas") incorporados com sensores, software e outras tecnologias com o propósito de conectar e trocar dados com outros dispositivos e sistemas pela internet. Isso permite que objetos do dia a dia coletem e troquem dados, criando um ambiente mais inteligente e responsivo.

*   **Arquitetura da IoT:** Geralmente envolve várias camadas:
    *   **Camada de Percepção (Sensores/Atuadores):** Coleta dados do ambiente (sensores) e interage com o mundo físico (atuadores).
    *   **Camada de Rede:** Transmite os dados coletados para a nuvem ou para outros dispositivos.
    *   **Camada de Processamento (Middleware):** Processa, armazena e analisa os dados.
    *   **Camada de Aplicação:** Fornece serviços e interfaces para os usuários finais.

*   **Sensores:** Dispositivos que detectam e respondem a estímulos do ambiente físico, convertendo-os em sinais elétricos. Exemplos: sensores de temperatura, umidade, movimento, luz, pressão, GPS.

*   **Protocolos IoT:** Protocolos de comunicação otimizados para dispositivos com recursos limitados e redes com baixa largura de banda:
    *   **MQTT (Message Queuing Telemetry Transport):** Um protocolo de mensagens leve, baseado em publish/subscribe, ideal para dispositivos IoT com restrições de energia e largura de banda. Amplamente utilizado para telemetria e comunicação máquina a máquina.
    *   **CoAP (Constrained Application Protocol):** Um protocolo web especializado para dispositivos restritos, semelhante ao HTTP, mas otimizado para ambientes IoT com baixa largura de banda e recursos limitados.

*   **Plataformas IoT:** Placas de desenvolvimento e microcontroladores populares para prototipagem e construção de dispositivos IoT:
    *   **Arduino:** Uma plataforma de hardware e software de código aberto, fácil de usar, ideal para iniciantes e projetos que exigem interação com o mundo físico através de sensores e atuadores.
    *   **Raspberry Pi:** Um computador de placa única (Single Board Computer - SBC) de baixo custo, com capacidade de processamento mais robusta que o Arduino, capaz de rodar um sistema operacional completo (como Linux) e executar tarefas mais complexas, como servidores web ou centros de mídia.

*   **Edge Computing:** É um paradigma de computação distribuída que aproxima o processamento de dados da fonte de geração dos dados (a "borda" da rede), em vez de enviá-los para um data center centralizado ou para a nuvem. Na IoT, isso significa processar dados diretamente nos dispositivos IoT ou em gateways próximos, reduzindo a latência, o consumo de largura de banda e melhorando a privacidade e a segurança. É crucial para aplicações que exigem respostas em tempo real.

#### Sexta-feira: Big Data e Data Science: conceitos de Hadoop, Spark, NoSQL. Ética e legislação (LGPD). Tendências: IA generativa, blockchain.

Esta aula aborda conceitos cruciais da era da informação e tendências tecnológicas:

*   **Big Data:** Refere-se a conjuntos de dados tão grandes e complexos que os métodos tradicionais de processamento de dados são inadequados. É caracterizado pelos "Vs":
    *   **Volume:** Grande quantidade de dados.
    *   **Velocidade:** Geração e processamento rápidos de dados.
    *   **Variedade:** Diversidade de formatos e tipos de dados (estruturados, semiestruturados, não estruturados).
    *   **Veracidade:** Qualidade e confiabilidade dos dados.
    *   **Valor:** Capacidade de extrair insights e valor dos dados.

*   **Data Science:** É um campo interdisciplinar que usa métodos científicos, processos, algoritmos e sistemas para extrair conhecimento e insights de dados estruturados e não estruturados. Envolve estatística, matemática, programação e conhecimento de domínio.

*   **Ferramentas para Big Data:**
    *   **Hadoop:** Um framework de código aberto para armazenar e processar grandes volumes de dados de forma distribuída em clusters de computadores. Inclui o HDFS (Hadoop Distributed File System) para armazenamento e o MapReduce para processamento.
    *   **Spark:** Um motor de processamento de dados distribuído e de código aberto, mais rápido que o MapReduce do Hadoop para muitas cargas de trabalho, especialmente para processamento em memória e interativo. Suporta SQL, streaming, machine learning e processamento de grafos.
    *   **NoSQL (Not Only SQL):** Bancos de dados que não seguem o modelo relacional tradicional. São projetados para lidar com grandes volumes de dados não estruturados ou semiestruturados, oferecendo alta escalabilidade e flexibilidade. Exemplos: MongoDB (documentos), Cassandra (colunas largas), Redis (chave-valor).

*   **Ética e Legislação (LGPD - Lei Geral de Proteção de Dados):** Com o aumento da coleta e processamento de dados, a ética e a legislação se tornaram fundamentais. A LGPD (no Brasil) e o GDPR (na Europa) são exemplos de leis que regulamentam a coleta, o armazenamento, o tratamento e o compartilhamento de dados pessoais, visando proteger a privacidade e os direitos dos indivíduos. Elas impõem obrigações às empresas e organizações que lidam com dados pessoais.

*   **Tendências Tecnológicas:**
    *   **IA Generativa:** Um subcampo da Inteligência Artificial que se concentra na criação de novos conteúdos (texto, imagens, áudio, vídeo) que são semelhantes aos dados de treinamento, mas não idênticos. Modelos como GPT (para texto) e DALL-E (para imagens) são exemplos proeminentes. Tem aplicações em criação de conteúdo, design, simulação e muito mais.
    *   **Blockchain:** Uma tecnologia de registro distribuído e descentralizado que armazena transações de forma segura e imutável em blocos encadeados criptograficamente. É a tecnologia por trás das criptomoedas (como Bitcoin) e tem aplicações em segurança de dados, rastreabilidade na cadeia de suprimentos, contratos inteligentes e votação eletrônica.

---
### Semana 7 – Revisão e Transição

#### Segunda-feira: Revisão geral do Módulo I (quiz mental com perguntas dos últimos 30 dias).

Neste dia, o foco é consolidar o conhecimento adquirido ao longo das últimas seis semanas do Módulo I. A revisão geral deve abordar os principais conceitos de **Fundamentos e Manutenção de Hardware**, **Introdução à Informática**, **Lógica Matemática Aplicada à Computação**, **Redes de Computadores** e **Sistemas Operacionais I**, além dos **Tópicos Especiais para Informática**.

Um **quiz mental** pode ser estruturado com perguntas que estimulem a lembrança e a aplicação dos conceitos. Exemplos de perguntas:

*   Qual a diferença fundamental entre hardware e software?
*   Cite os principais componentes internos de um computador e suas funções.
*   Explique a diferença entre arquitetura CISC e RISC em processadores.
*   O que é memória RAM e quais suas características (DDR, frequência, latência)?
*   Compare HDD e SSD em termos de tecnologia, velocidade e durabilidade.
*   O que é um barramento e qual sua importância na arquitetura do computador?
*   Qual a função do chipset na placa-mãe?
*   Explique a Lei de Moore e sua relevância.
*   Converta um número decimal para binário e hexadecimal.
*   Qual a diferença entre bit e byte?
*   O que são ASCII e Unicode e por que o Unicode é mais abrangente?
*   Defina proposição e cite os principais conectivos lógicos.
*   Construa a tabela-verdade para uma expressão lógica simples.
*   Explique as Leis de De Morgan e sua aplicação.
*   Quais são as portas lógicas básicas e como elas funcionam?
*   O que são quantificadores universal e existencial na lógica de predicados?
*   Cite exemplos de aplicações da lógica matemática em circuitos aritméticos.
*   Diferencie LAN, WAN e MAN.
*   Explique o Modelo OSI e o Modelo TCP/IP, citando suas camadas.
*   O que é encapsulamento e PDU?
*   Qual a função do protocolo IP e do TCP?
*   Diferencie IPv4 e IPv6.
*   O que é uma máscara de rede e um gateway?
*   Explique o funcionamento de um roteador e de um switch.
*   O que é uma VLAN e para que serve?
*   Como o NAT ajuda a economizar endereços IPv4?
*   Qual a importância do DHCP em uma rede?
*   O que é um firewall e como ele protege a rede?
*   Explique o conceito de VPN.
*   Qual a diferença entre IDS e IPS?
*   O que é SDN e quais suas vantagens?
*   Como o Wireshark é usado na análise de tráfego de rede?
*   Defina Sistema Operacional e suas funções principais.
*   Quais são os estados de um processo?
*   Explique os algoritmos de escalonamento FCFS, SJF e Round Robin.
*   Qual a diferença entre processo e thread?
*   O que são condições de corrida e como semáforos/mutexes as previnem?
*   Quais as condições para um deadlock ocorrer?
*   Explique paginação e segmentação no gerenciamento de memória.
*   O que é memória virtual e page fault?
*   O que é thrashing e como evitá-lo?
*   Compare FAT32, NTFS e ext4.
*   Qual a função de um inode e do journaling?
*   Como funcionam as permissões de arquivo em sistemas Unix/Linux e Windows?
*   Cite exemplos de software aplicativo para edição de texto e planilhas.
*   O que são macros e VBA no Excel?
*   Explique os modelos de serviço da computação em nuvem (IaaS, PaaS, SaaS).
*   O que é IoT e quais seus componentes básicos?
*   Diferencie Arduino e Raspberry Pi.
*   O que é Edge Computing?
*   Defina Big Data e seus "Vs".
*   Qual a diferença entre Hadoop e Spark?
*   O que são bancos de dados NoSQL?
*   Qual a importância da LGPD?
*   Explique o conceito de IA Generativa e Blockchain.

#### Terça-feira: Exercícios práticos: montagem virtual de PC, cálculo de sub-rede, análise de logs de SO.

Este dia é dedicado à aplicação prática dos conhecimentos teóricos adquiridos. A realização de exercícios práticos ajuda a solidificar o aprendizado e a desenvolver habilidades de resolução de problemas.

*   **Montagem Virtual de PC:** Utilizar simuladores online ou softwares específicos (como o Cisco Packet Tracer para hardware, ou simuladores de montagem de PC) para praticar a identificação e conexão correta dos componentes de hardware (placa-mãe, CPU, RAM, GPU, armazenamento, fonte de alimentação). Isso reforça o entendimento da função de cada peça e da compatibilidade entre elas.

*   **Cálculo de Sub-rede (Subnetting):** Resolver problemas de cálculo de sub-redes IPv4, determinando endereços de rede, broadcast, faixas de hosts válidos e máscaras de sub-rede para diferentes cenários. Isso é crucial para o planejamento e a configuração de redes eficientes e seguras. Pode-se usar exemplos com CIDR para praticar a flexibilidade do endereçamento.

*   **Análise de Logs de SO:** Examinar logs de sistemas operacionais (Windows Event Viewer, logs do Linux em `/var/log`) para identificar eventos importantes, erros, avisos e atividades suspeitas. Isso desenvolve a capacidade de diagnosticar problemas de sistema, monitorar a segurança e entender o comportamento do SO em diferentes situações.

#### Quarta-feira: Discussão sobre boas práticas de estudo e aprofundamento (canais, livros, certificações).

Além do conteúdo técnico, é fundamental orientar sobre como continuar aprendendo e se desenvolvendo na área de TI. Este dia foca em estratégias de aprendizado contínuo:

*   **Boas Práticas de Estudo:**
    *   **Estudo Ativo:** Não apenas ler, mas fazer anotações, resumir, explicar os conceitos para si mesmo ou para outros.
    *   **Prática Constante:** A teoria sem a prática é insuficiente. Realizar projetos, exercícios e experimentos.
    *   **Resolução de Problemas:** Enfrentar desafios e buscar soluções, desenvolvendo o pensamento crítico.
    *   **Comunidade:** Participar de fóruns, grupos de estudo, eventos e comunidades online para trocar conhecimentos e experiências.
    *   **Descanso e Revisão:** Garantir pausas e revisões periódicas para fixar o conteúdo.

*   **Canais e Recursos para Aprofundamento:**
    *   **Canais do YouTube:** Sugerir canais relevantes de tecnologia, programação, redes, etc.
    *   **Plataformas de Cursos Online:** Coursera, Udemy, Alura, DIO, edX, etc.
    *   **Documentação Oficial:** Incentivar a leitura da documentação de tecnologias e ferramentas.
    *   **Blogs e Artigos Técnicos:** Indicar blogs de referência e sites especializados.

*   **Livros Recomendados:** Sugerir livros clássicos e atuais sobre os temas abordados no Módulo I (ex: "Redes de Computadores" de Tanenbaum, "Sistemas Operacionais Modernos" de Tanenbaum, livros sobre lógica digital e arquitetura de computadores).

*   **Certificações:** Discutir a importância das certificações na carreira de TI e apresentar algumas opções relevantes para os temas do Módulo I:
    *   **CompTIA A+:** Certificação de entrada que valida conhecimentos em hardware e software de PC.
    *   **CompTIA Network+:** Foca em fundamentos de rede.
    *   **LPIC (Linux Professional Institute Certification):** Certificações para profissionais Linux.
    *   **Certificações de Fornecedores:** Cisco CCNA (redes), Microsoft Certified: Azure Fundamentals (nuvem), AWS Certified Cloud Practitioner (nuvem).

#### Quinta-feira: Introdução ao Módulo II: visão geral de automação, gestão e eletrônica.

Este dia serve como uma ponte para o próximo módulo, preparando o aluno para os novos tópicos que serão abordados. A introdução deve fornecer uma visão geral e despertar o interesse.

*   **Visão Geral do Módulo II:** Apresentar os três pilares principais do Módulo II:
    *   **Gerência:** Abordará conceitos de gerência de projetos em TI, planejamento estratégico e empreendedorismo, preparando o aluno para liderar e organizar iniciativas.
    *   **Automação:** Explorará os fundamentos da automação, desde sensores e atuadores até CLPs e sistemas supervisórios, mostrando como a tecnologia pode otimizar processos.
    *   **Eletrônica:** Introduzirá os conceitos básicos de eletrônica, componentes passivos e ativos, circuitos integrados e sistemas embarcados, fornecendo a base para entender o funcionamento físico dos sistemas.

*   **Conexão com o Módulo I:** Explicar como os conhecimentos adquiridos no Módulo I (hardware, software, redes, SO) são a base para o Módulo II, mostrando a interconexão entre as áreas da informática.

*   **Expectativas para o Módulo II:** Destacar a relevância desses temas para o mercado de trabalho e como eles se complementam para formar um profissional mais completo e versátil.

#### Sexta-feira: Feriado / flexível (ou reforço opcional).

Este dia é designado como **feriado ou flexível**, oferecendo uma pausa no cronograma formal. No entanto, pode ser utilizado para **reforço opcional** para aqueles que desejam aprofundar algum tópico específico do Módulo I ou revisar conceitos que consideraram mais desafiadores. Sugestões para o dia flexível:

*   **Revisão Aprofundada:** Relembrar os tópicos do quiz de segunda-feira que foram mais difíceis.
*   **Projetos Pessoais:** Iniciar um pequeno projeto prático relacionado a hardware, redes ou sistemas operacionais.
*   **Leitura Complementar:** Explorar os livros ou artigos sugeridos na quarta-feira.
*   **Exploração de Ferramentas:** Instalar e experimentar ferramentas como Wireshark, simuladores de rede ou ambientes de desenvolvimento.
*   **Descanso:** Aproveitar o dia para recarregar as energias, o que também é fundamental para o aprendizado eficaz.

---
## Módulo II – GERÊNCIA, AUTOMAÇÃO E ELETRÔNICA

### Semana 8 – Elementos de Automação

#### Segunda-feira: O que é automação? Histórico (pneumática, relés, CLPs). Arquitetura de sistemas automatizados: sensores, atuadores, controladores.

A **automação** é a aplicação de tecnologia para tornar um processo ou sistema autônomo, reduzindo ou eliminando a necessidade de intervenção humana. O objetivo principal é aumentar a eficiência, a produtividade, a segurança e a qualidade, ao mesmo tempo em que se reduzem custos e erros. A automação está presente em diversas áreas, desde a indústria até o cotidiano, como em sistemas de casas inteligentes.

**Histórico da Automação:**

*   **Pneumática e Hidráulica:** As primeiras formas de automação industrial utilizavam sistemas baseados em ar comprimido (pneumática) ou fluidos (hidráulica) para movimentar máquinas e controlar processos. Esses sistemas são robustos e ainda são usados em muitas aplicações.
*   **Relés:** Com o advento da eletricidade, os relés se tornaram componentes fundamentais. Um relé é um interruptor eletromecânico que abre ou fecha circuitos elétricos com base em um sinal de controle. A combinação de relés permitia a criação de lógicas de controle sequenciais, sendo a base para os primeiros sistemas de automação elétrica.
*   **CLPs (Controladores Lógicos Programáveis):** Surgiram na década de 1960 para substituir os painéis de relés, que eram complexos, caros e difíceis de modificar. Um CLP é um computador industrial robusto, projetado para controlar processos de fabricação. Ele recebe sinais de entrada (sensores), executa um programa lógico e envia sinais de saída (atuadores). A programação é feita em linguagens específicas, como Ladder Diagram, que se assemelha aos diagramas de relés.

**Arquitetura de Sistemas Automatizados:** Um sistema automatizado típico é composto por três elementos principais que trabalham em conjunto:

*   **Sensores:** São os "olhos" e "ouvidos" do sistema. Dispositivos que detectam e medem grandezas físicas (temperatura, pressão, presença, nível, etc.) e as convertem em sinais elétricos que podem ser interpretados pelo controlador. Exemplos: termopares, sensores de proximidade, fotocélulas.
*   **Atuadores:** São os "músculos" do sistema. Dispositivos que convertem sinais elétricos do controlador em ações físicas, como movimento, abertura/fechamento de válvulas, acionamento de motores. Exemplos: motores elétricos, válvulas solenoides, cilindros pneumáticos.
*   **Controladores:** São o "cérebro" do sistema. Recebem os sinais dos sensores, processam as informações de acordo com um programa lógico (implementado em CLPs, microcontroladores ou computadores industriais) e enviam comandos para os atuadores, fechando o ciclo de controle. O controlador toma decisões para manter o processo dentro dos parâmetros desejados.

#### Terça-feira: Sensores: tipos (indutivos, capacitivos, ópticos, ultrassônicos). Características (alcance, histerese, NPN/PNP).

Os **sensores** são componentes cruciais em sistemas automatizados, responsáveis por coletar informações do ambiente e convertê-las em sinais elétricos. Existem diversos tipos, cada um adequado para diferentes aplicações:

*   **Tipos de Sensores de Proximidade (para detecção de objetos):**
    *   **Indutivos:** Detectam a presença de objetos metálicos sem contato físico. Funcionam gerando um campo eletromagnético e detectando alterações nesse campo quando um metal se aproxima. São robustos e imunes a sujeira.
    *   **Capacitivos:** Detectam a presença de qualquer tipo de material (metálico ou não metálico, sólido ou líquido) sem contato físico. Funcionam detectando alterações na capacitância do campo elétrico gerado. Úteis para detectar nível de líquidos em tanques não metálicos.
    *   **Ópticos:** Detectam a presença ou ausência de objetos usando luz (infravermelha, visível). Podem ser do tipo barreira (emissor e receptor separados), difuso (emissor e receptor no mesmo corpo, detecta a luz refletida pelo objeto) ou retro-reflexivo (emissor e receptor no mesmo corpo, com um refletor). São versáteis e detectam diversos materiais.
    *   **Ultrassônicos:** Detectam a presença e a distância de objetos usando ondas sonoras de alta frequência. Emitem um pulso ultrassônico e medem o tempo que leva para o eco retornar. São ideais para medir distâncias e detectar objetos transparentes ou de cores variadas.

*   **Características Importantes dos Sensores:**
    *   **Alcance (Distância de Detecção):** A distância máxima na qual o sensor consegue detectar um objeto de forma confiável. Varia muito entre os tipos e modelos de sensores.
    *   **Histerese:** É a diferença entre o ponto de atuação (quando o sensor liga) e o ponto de desatuação (quando o sensor desliga). Ajuda a evitar oscilações indesejadas na saída do sensor quando o objeto está na borda da zona de detecção.
    *   **Saída NPN/PNP:** Refere-se ao tipo de transistor de saída do sensor, que determina como ele se conecta ao circuito de controle:
        *   **NPN (Negative-Positive-Negative):** A saída do sensor "afunda" a corrente (sink current), ou seja, conecta a carga ao negativo (GND) quando ativado. A carga é conectada entre a saída do sensor e o positivo da fonte.
        *   **PNP (Positive-Negative-Positive):** A saída do sensor "fornece" a corrente (source current), ou seja, conecta a carga ao positivo da fonte quando ativado. A carga é conectada entre a saída do sensor e o negativo (GND).

#### Quarta-feira: Atuadores: motores (DC, passo, servo), válvulas, relés. Controle por PWM e driver de potência.

Os **atuadores** são os dispositivos que convertem energia (elétrica, pneumática, hidráulica) em movimento ou ação física, executando os comandos enviados pelo controlador. Eles são essenciais para interagir com o ambiente físico em sistemas automatizados.

*   **Tipos de Atuadores Comuns:**
    *   **Motores DC (Corrente Contínua):** Motores elétricos simples que giram continuamente quando energizados. A velocidade e o sentido de rotação podem ser controlados variando a tensão e a polaridade. São amplamente usados em robótica, brinquedos e aplicações de baixa potência.
    *   **Motores de Passo (Stepper Motors):** Motores que giram em passos discretos e precisos. Permitem um controle exato da posição e da velocidade sem a necessidade de feedback (em malha aberta). São ideais para aplicações que exigem posicionamento preciso, como impressoras 3D, CNCs e leitores de disco.
    *   **Servomotores (Servos):** Motores que permitem um controle preciso do ângulo de rotação. Possuem um sistema de feedback (geralmente um potenciômetro) que informa a posição atual, permitindo um controle em malha fechada. São usados em robótica, aeromodelismo e aplicações que exigem posicionamento angular exato.
    *   **Válvulas Solenoides:** Dispositivos eletromecânicos que controlam o fluxo de fluidos (líquidos ou gases) através de um orifício. Quando energizadas, um campo magnético move um êmbolo que abre ou fecha a passagem. Usadas em sistemas pneumáticos, hidráulicos e de irrigação.
    *   **Relés:** Embora já mencionados como parte do histórico, os relés também atuam como atuadores, pois permitem que um sinal de baixa potência (do controlador) controle um circuito de alta potência (ex: ligar/desligar uma lâmpada ou motor).

*   **Controle de Atuadores:**
    *   **PWM (Pulse Width Modulation - Modulação por Largura de Pulso):** É uma técnica para controlar a potência média fornecida a um dispositivo eletrônico, como um motor ou LED, variando a largura dos pulsos de um sinal digital. Ao variar o ciclo de trabalho (duty cycle) do pulso (proporção de tempo em que o sinal está ligado), é possível controlar a velocidade de um motor DC, o brilho de um LED ou a posição de um servomotor.
    *   **Driver de Potência:** São circuitos eletrônicos projetados para fornecer a corrente e a tensão necessárias para acionar atuadores de maior potência, como motores. Os microcontroladores e CLPs geralmente não conseguem fornecer corrente suficiente diretamente para esses atuadores, então um driver de potência atua como uma interface entre o controlador e o atuador, amplificando o sinal de controle.

#### Quinta-feira: CLP (Controlador Lógico Programável): linguagens (Ladder, FBD, ST). Programação básica: contatos, bobinas, timers, contadores.

O **CLP (Controlador Lógico Programável)** é um computador industrial robusto, projetado especificamente para automatizar processos industriais. Ele monitora entradas (sensores), executa um programa lógico e controla saídas (atuadores). Sua principal vantagem é a flexibilidade de programação e a capacidade de operar em ambientes industriais adversos.

**Linguagens de Programação de CLP (padrão IEC 61131-3):**

*   **Ladder Diagram (LD):** A linguagem mais popular e visualmente intuitiva, desenvolvida para se assemelhar aos diagramas de circuitos de relés. É ideal para eletricistas e técnicos, utilizando símbolos gráficos para contatos (normalmente abertos/fechados) e bobinas.
*   **Function Block Diagram (FBD):** Uma linguagem gráfica que representa a lógica de controle como blocos de funções interconectados. Cada bloco realiza uma função específica (ex: temporizador, contador, operação matemática). É útil para visualizar o fluxo de dados e controle.
*   **Structured Text (ST):** Uma linguagem de programação textual de alto nível, semelhante a Pascal ou C. É poderosa e flexível, ideal para algoritmos complexos, cálculos matemáticos e manipulação de dados. Preferida por programadores com experiência em linguagens textuais.
*   **Instruction List (IL):** Uma linguagem de baixo nível, semelhante a assembly, que usa mnemônicos para representar instruções. É compacta, mas menos legível para lógicas complexas.
*   **Sequential Function Chart (SFC):** Uma linguagem gráfica que organiza o programa em passos e transições, ideal para processos sequenciais e máquinas de estado.

**Programação Básica de CLP (em Ladder Diagram):**

*   **Contatos:** Representam as entradas (sensores, botões) ou condições lógicas. Podem ser:
    *   **Normalmente Aberto (NA):** Permite a passagem de corrente quando ativado (ex: botão pressionado, sensor detecta).
    *   **Normalmente Fechado (NF):** Bloqueia a passagem de corrente quando ativado (ex: botão solto, sensor não detecta).
*   **Bobinas:** Representam as saídas (atuadores, lâmpadas) ou variáveis internas (memórias). São ativadas quando a lógica à esquerda da bobina é verdadeira.
*   **Timers (Temporizadores):** Blocos de função que medem o tempo. Os tipos comuns são:
    *   **TON (Timer ON Delay):** Liga a saída após um tempo pré-definido, desde que a entrada permaneça ativa.
    *   **TOF (Timer OFF Delay):** Desliga a saída após um tempo pré-definido, após a entrada ser desativada.
    *   **TP (Timer Pulse):** Gera um pulso de saída por um tempo pré-definido.
*   **Contadores (Counters):** Blocos de função que contam eventos. Os tipos comuns são:
    *   **CTU (Count Up):** Incrementa um valor a cada pulso na entrada de contagem.
    *   **CTD (Count Down):** Decrementa um valor a cada pulso na entrada de contagem.
    *   **CTUD (Count Up/Down):** Combina as funcionalidades de contagem crescente e decrescente.

#### Sexta-feira: Automação avançada: supervisório (SCADA), protocolos industriais (Modbus, Profibus). Indústria 4.0, IIoT, gêmeos digitais.

À medida que os sistemas de automação se tornam mais complexos e interconectados, surgem conceitos e tecnologias avançadas:

*   **Sistemas Supervisórios (SCADA - Supervisory Control and Data Acquisition):** São sistemas de software que permitem monitorar e controlar processos industriais em tempo real a partir de uma estação central. Um sistema SCADA coleta dados de CLPs e outros dispositivos de campo, exibe-os em interfaces gráficas (HMIs - Human Machine Interfaces), registra históricos, gera alarmes e permite que os operadores enviem comandos de controle. É fundamental para a operação e otimização de grandes plantas industriais.

*   **Protocolos Industriais:** São padrões de comunicação que permitem que diferentes dispositivos e sistemas em um ambiente industrial troquem dados de forma padronizada:
    *   **Modbus:** Um dos protocolos mais antigos e amplamente utilizados, conhecido por sua simplicidade e robustez. Permite a comunicação entre CLPs, HMIs e outros dispositivos.
    *   **Profibus (Process Field Bus):** Um protocolo de comunicação de campo mais avançado, com maior velocidade e capacidade de comunicação. É amplamente utilizado em automação de processos e manufatura.
    *   Outros protocolos incluem Ethernet/IP, PROFINET, CANopen, entre outros.

*   **Indústria 4.0:** É a quarta revolução industrial, caracterizada pela fusão de tecnologias digitais, físicas e biológicas. Ela envolve a digitalização e a integração de processos de fabricação, resultando em fábricas inteligentes, autônomas e conectadas. Os pilares da Indústria 4.0 incluem:
    *   **Sistemas Ciber-Físicos (CPS):** Integração de computação e processos físicos.
    *   **Internet das Coisas Industrial (IIoT):** Aplicação da IoT em ambientes industriais.
    *   **Big Data e Análise de Dados:** Para otimização de processos e manutenção preditiva.
    *   **Inteligência Artificial e Machine Learning:** Para automação avançada e tomada de decisão.
    *   **Manufatura Aditiva (Impressão 3D):** Para prototipagem e produção flexível.
    *   **Robótica Avançada e Colaborativa:** Robôs que trabalham ao lado de humanos.

*   **IIoT (Industrial Internet of Things - Internet das Coisas Industrial):** É a aplicação da tecnologia IoT em ambientes industriais. Envolve a conexão de máquinas, sensores e dispositivos em fábricas e plantas industriais para coletar e analisar dados em tempo real. O objetivo é otimizar a produção, prever falhas de equipamentos (manutenção preditiva), melhorar a eficiência energética e aumentar a segurança.

*   **Gêmeos Digitais (Digital Twins):** São representações virtuais de objetos, processos ou sistemas físicos. Um gêmeo digital é alimentado com dados em tempo real de sensores no objeto físico, permitindo simulações, análises e monitoramento do comportamento do objeto no mundo real. Isso possibilita otimizar o desempenho, prever problemas e testar cenários antes de implementá-los fisicamente, reduzindo riscos e custos.

---
### Semana 9 – Introdução à Eletrônica

#### Segunda-feira: Fundamentos: tensão, corrente, resistência, potência (Lei de Ohm). Circuitos série e paralelo. Multímetro.

A **eletrônica** é o ramo da física e da engenharia que estuda o controle do fluxo de elétrons para realizar tarefas. Para compreender os circuitos eletrônicos, é fundamental dominar alguns conceitos básicos:

*   **Tensão (Voltagem - V):** É a força ou pressão elétrica que impulsiona os elétrons através de um circuito. Medida em Volts (V), a tensão é a diferença de potencial elétrico entre dois pontos. É o que faz a corrente fluir.
*   **Corrente (I):** É o fluxo de elétrons através de um condutor. Medida em Ampères (A), a corrente é a quantidade de carga elétrica que passa por um ponto em um determinado tempo. É o que realiza o trabalho no circuito.
*   **Resistência (R):** É a oposição ao fluxo de corrente elétrica em um material. Medida em Ohms (Ω), a resistência limita a quantidade de corrente que pode fluir para uma dada tensão. Materiais com alta resistência são isolantes; com baixa resistência, são condutores.
*   **Potência (P):** É a taxa na qual a energia elétrica é consumida ou produzida em um circuito. Medida em Watts (W), a potência é o produto da tensão pela corrente (P = V * I). É a capacidade de realizar trabalho.

*   **Lei de Ohm:** É uma das leis fundamentais da eletrônica, que descreve a relação entre tensão, corrente e resistência em um circuito. Ela afirma que a corrente (I) que flui através de um condutor entre dois pontos é diretamente proporcional à tensão (V) entre esses dois pontos e inversamente proporcional à resistência (R) do condutor. Matematicamente, é expressa como: **V = I * R**.

*   **Circuitos Série e Paralelo:**
    *   **Circuito Série:** Os componentes são conectados um após o outro, formando um único caminho para a corrente. A corrente é a mesma em todos os pontos do circuito, mas a tensão se divide entre os componentes. A resistência total é a soma das resistências individuais.
    *   **Circuito Paralelo:** Os componentes são conectados em caminhos separados, de modo que a corrente se divide entre eles. A tensão é a mesma em todos os componentes, mas a corrente se divide. A resistência total é menor que a menor resistência individual.

*   **Multímetro:** É uma ferramenta essencial para qualquer eletrônico. Ele combina as funções de um voltímetro (mede tensão), amperímetro (mede corrente) e ohmímetro (mede resistência). Multímetros digitais modernos também podem medir capacitância, frequência, temperatura, entre outros. É usado para diagnosticar problemas, verificar componentes e medir grandezas elétricas em circuitos.

#### Terça-feira: Componentes passivos: resistor (código de cores), capacitor (carga/descarga), indutor. Associações.

Os **componentes passivos** são elementos de circuito que não geram energia, mas a armazenam, dissipam ou a controlam. Eles são fundamentais para moldar o comportamento dos circuitos eletrônicos.

*   **Resistor:** É um componente que oferece resistência à passagem da corrente elétrica, convertendo energia elétrica em calor. Sua principal função é limitar a corrente, dividir a tensão e polarizar transistores. O valor da resistência é medido em Ohms (Ω).
    *   **Código de Cores:** A maioria dos resistores de pequeno porte tem seu valor de resistência indicado por faixas coloridas. Cada cor representa um dígito, um multiplicador e uma tolerância. É fundamental saber decifrar esse código para identificar o valor correto do resistor.

*   **Capacitor:** É um componente que armazena energia elétrica em um campo elétrico. Consiste em duas placas condutoras separadas por um material dielétrico. Sua principal função é filtrar ruídos, armazenar energia temporariamente, acoplar e desacoplar sinais. A capacidade de armazenamento é medida em Farads (F), mas geralmente são usados submúltiplos como microfarads (µF), nanofarads (nF) e picofarads (pF).
    *   **Carga e Descarga:** Quando um capacitor é conectado a uma fonte de tensão, ele se carrega, armazenando energia. Quando a fonte é removida, ele se descarrega, liberando a energia armazenada. O tempo de carga/descarga depende da capacitância e da resistência do circuito.

*   **Indutor:** É um componente que armazena energia em um campo magnético quando uma corrente elétrica passa por ele. Consiste em um fio enrolado em forma de bobina. Sua principal função é filtrar sinais, armazenar energia e criar campos magnéticos. A indutância é medida em Henrys (H).

*   **Associações de Componentes:** Assim como resistores, capacitores e indutores podem ser associados em série ou paralelo, e as regras para calcular a resistência/capacitância/indutância equivalente variam:
    *   **Resistores:** Em série, a resistência total é a soma. Em paralelo, o inverso da resistência total é a soma dos inversos.
    *   **Capacitores:** Em série, o inverso da capacitância total é a soma dos inversos. Em paralelo, a capacitância total é a soma.
    *   **Indutores:** Em série, a indutância total é a soma. Em paralelo, o inverso da indutância total é a soma dos inversos.

#### Quarta-feira: Componentes ativos: diodo (retificador, LED, Zener), transistor (BJT e MOSFET como chave e amplificador).

Os **componentes ativos** são elementos de circuito que podem controlar o fluxo de corrente elétrica e, em alguns casos, gerar energia ou amplificar sinais. Eles são a base da eletrônica moderna.

*   **Diodo:** É um componente semicondutor que permite que a corrente elétrica flua em uma única direção (polarização direta) e bloqueia o fluxo na direção oposta (polarização reversa). Possui dois terminais: anodo (+) e catodo (-).
    *   **Diodo Retificador:** Usado para converter corrente alternada (AC) em corrente contínua (DC), um processo chamado retificação. É fundamental em fontes de alimentação.
    *   **LED (Light Emitting Diode - Diodo Emissor de Luz):** Um tipo especial de diodo que emite luz quando polarizado diretamente. Amplamente usado em iluminação, displays e indicadores.
    *   **Diodo Zener:** Projetado para operar na região de ruptura reversa. É usado para regular a tensão, mantendo uma tensão de saída constante, mesmo que a tensão de entrada ou a carga variem.

*   **Transistor:** É um componente semicondutor que atua como um interruptor eletrônico ou um amplificador de sinal. É o bloco construtivo fundamental de todos os circuitos integrados e processadores. Existem dois tipos principais:
    *   **BJT (Bipolar Junction Transistor):** Possui três terminais: base, coletor e emissor. Uma pequena corrente na base controla uma corrente maior entre coletor e emissor. Pode ser usado como chave (ligar/desligar) ou como amplificador de sinal.
    *   **MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor):** Possui três terminais: gate, drain e source. Uma tensão no gate controla a corrente entre drain e source. É amplamente utilizado em circuitos digitais (como em microprocessadores) e em aplicações de potência devido à sua alta impedância de entrada e eficiência como chave.

#### Quinta-feira: Circuitos integrados: CI 555, amplificadores operacionais (comparador, seguidor de tensão). Fonte de alimentação regulada.

Os **circuitos integrados (CIs)** são pequenos chips que contêm milhares ou milhões de componentes eletrônicos (transistores, resistores, capacitores) interconectados em uma única pastilha de semicondutor. Eles revolucionaram a eletrônica, permitindo a criação de dispositivos complexos em tamanhos reduzidos.

*   **CI 555 (Timer 555):** É um dos circuitos integrados mais versáteis e populares. É um temporizador que pode operar em três modos principais:
    *   **Monoestável:** Gera um único pulso de duração controlada em resposta a um gatilho.
    *   **Astable:** Gera uma sequência contínua de pulsos (onda quadrada), funcionando como um oscilador.
    *   **Biestável:** Atua como um flip-flop, com dois estados estáveis.
    É amplamente utilizado em temporizadores, osciladores, geradores de pulso, moduladores PWM e muito mais.

*   **Amplificadores Operacionais (Amp-Op):** São CIs de alta ganho, com duas entradas (inversora e não-inversora) e uma saída. São extremamente versáteis e podem ser configurados para realizar uma vasta gama de operações, como:
    *   **Comparador:** Compara duas tensões de entrada e produz uma saída alta ou baixa dependendo de qual entrada é maior.
    *   **Seguidor de Tensão (Buffer):** Possui um ganho de tensão unitário e uma alta impedância de entrada, sendo usado para isolar um estágio de circuito de outro, evitando que a carga afete a fonte de sinal.
    *   Outras aplicações incluem amplificadores, somadores, integradores, diferenciadores e filtros.

*   **Fonte de Alimentação Regulada:** É um circuito que fornece uma tensão de saída constante e estável, independentemente das variações na tensão de entrada ou na carga. Uma fonte regulada típica consiste em:
    *   **Transformador:** Reduz a tensão AC da rede elétrica.
    *   **Retificador:** Converte a tensão AC em DC pulsante (geralmente com diodos).
    *   **Filtro:** Suaviza a tensão DC pulsante (geralmente com capacitores).
    *   **Regulador de Tensão:** Mantém a tensão de saída constante (geralmente com diodos Zener ou CIs reguladores de tensão, como a série LM78xx).
    Fontes reguladas são essenciais para alimentar circuitos eletrônicos sensíveis, garantindo seu funcionamento correto e protegendo-os contra flutuações de energia.

#### Sexta-feira: Eletrônica digital e embedded: Arduino (GPIO, PWM, ADC). Projeto de um semáforo com LEDs. Introdução à soldagem e protoboard.

A **eletrônica digital** lida com sinais discretos (0s e 1s) e é a base dos computadores e sistemas embarcados. Os **sistemas embarcados (embedded systems)** são sistemas computacionais projetados para realizar funções específicas dentro de um sistema maior, geralmente com restrições de tempo real e recursos.

*   **Arduino:** É uma plataforma de prototipagem eletrônica de código aberto, baseada em hardware e software flexíveis e fáceis de usar. É ideal para artistas, designers, hobbistas e qualquer pessoa interessada em criar objetos ou ambientes interativos. A placa Arduino possui um microcontrolador que pode ser programado para interagir com o mundo físico.
    *   **GPIO (General Purpose Input/Output - Entradas/Saídas de Propósito Geral):** São pinos digitais na placa Arduino que podem ser configurados como entrada (para ler sinais de sensores, botões) ou como saída (para controlar LEDs, relés, motores).
    *   **PWM (Pulse Width Modulation - Modulação por Largura de Pulso):** Alguns pinos do Arduino suportam PWM, permitindo simular saídas analógicas (ex: controlar o brilho de um LED, a velocidade de um motor DC) usando sinais digitais.
    *   **ADC (Analog-to-Digital Converter - Conversor Analógico-Digital):** Permite que o Arduino leia sinais analógicos (como os de sensores de temperatura ou potenciômetros) e os converta em valores digitais que o microcontrolador pode processar.

*   **Projeto de um Semáforo com LEDs:** Um projeto clássico para iniciantes em Arduino. Envolve:
    *   Conectar LEDs (vermelho, amarelo, verde) aos pinos GPIO do Arduino, usando resistores para limitar a corrente.
    *   Escrever um código (em linguagem C/C++ simplificada, usando a IDE do Arduino) que acenda e apague os LEDs em uma sequência que simule o funcionamento de um semáforo, utilizando funções de atraso (delay) e controle de pinos digitais.
    *   Este projeto ensina conceitos básicos de programação, controle de E/S e temporização.

*   **Introdução à Soldagem:** A soldagem é a técnica de unir componentes eletrônicos a uma placa de circuito impresso (PCB) usando solda (uma liga metálica de baixo ponto de fusão). É uma habilidade fundamental para construir e reparar circuitos eletrônicos. Envolve o uso de um ferro de solda, solda e fluxo.

*   **Protoboard (Breadboard):** É uma placa de ensaio sem solda, usada para montar protótipos de circuitos eletrônicos de forma temporária. Permite conectar componentes e fios facilmente, sem a necessidade de soldagem, o que é ideal para testar e depurar circuitos antes de finalizá-los em uma PCB.

---
### Semana 10 – Engenharia de Software (básico → avançado)

#### Segunda-feira: Conceitos: software, engenharia de software, diferença para programação. Ciclo de vida clássico (cascata).

Para desenvolver sistemas de software de forma eficiente e com qualidade, é fundamental compreender os conceitos de **software** e **engenharia de software**, bem como a diferença em relação à **programação**.

*   **Software:** Refere-se a um conjunto de instruções, dados ou programas usados para operar computadores e executar tarefas específicas. É a parte lógica e intangível de um sistema computacional, que permite ao hardware funcionar e interagir com o usuário. O software pode ser classificado em software de sistema (como sistemas operacionais) e software aplicativo (como editores de texto, jogos).

*   **Programação:** É o processo de escrever, testar e manter o código-fonte de um programa de computador. É uma atividade técnica que foca na implementação de algoritmos e na codificação de instruções em uma linguagem de programação específica. A programação é uma parte essencial do desenvolvimento de software, mas não abrange todo o processo.

*   **Engenharia de Software:** É uma disciplina que aplica uma abordagem sistemática, disciplinada e quantificável ao desenvolvimento, operação e manutenção de software. Ela vai além da simples programação, abrangendo todas as fases do ciclo de vida do software, desde a concepção e análise de requisitos até a implantação e manutenção. O objetivo é produzir software de alta qualidade, dentro do prazo e do orçamento, que atenda às necessidades do usuário.

    **Diferença para Programação:** Enquanto a programação é a construção do código, a engenharia de software é o processo de projetar, construir e manter sistemas de software complexos, considerando aspectos como gerenciamento de projetos, qualidade, segurança, escalabilidade e custo. A programação é uma tática; a engenharia de software é a estratégia.

*   **Ciclo de Vida Clássico (Modelo Cascata):** É um dos primeiros e mais tradicionais modelos de ciclo de vida de desenvolvimento de software. Ele é sequencial e linear, com cada fase sendo concluída antes que a próxima comece. As fases típicas são:
    1.  **Requisitos:** Levantamento e análise detalhada das necessidades do usuário e do sistema.
    2.  **Projeto (Design):** Definição da arquitetura do software, estruturas de dados, interfaces e algoritmos.
    3.  **Implementação (Codificação):** Escrita do código-fonte do software com base no projeto.
    4.  **Teste:** Verificação e validação do software para garantir que ele atenda aos requisitos e esteja livre de defeitos.
    5.  **Implantação:** Instalação e configuração do software no ambiente do usuário.
    6.  **Manutenção:** Correção de erros, adaptação a novas plataformas e melhorias contínuas.

    **Vantagens:** Simples de entender e gerenciar, bom para projetos com requisitos bem definidos e estáveis. **Desvantagens:** Pouca flexibilidade para mudanças, detecção tardia de erros, dificuldade em lidar com requisitos ambíguos.

#### Terça-feira: Modelos de processo: cascata, iterativo, espiral, incremental. Agile (Scrum, Kanban, XP).

Os **modelos de processo de software** são estruturas que descrevem a sequência de atividades e tarefas envolvidas no desenvolvimento de software. Eles fornecem uma abordagem sistemática para gerenciar a complexidade e garantir a qualidade. Além do modelo cascata, existem outros modelos importantes:

*   **Modelo Iterativo:** O desenvolvimento é dividido em pequenas iterações (ciclos), onde cada iteração produz uma versão funcional do software com funcionalidades adicionais. O feedback é coletado ao final de cada iteração para refinar os requisitos e o projeto. Permite maior flexibilidade e detecção precoce de problemas.

*   **Modelo Espiral:** Combina elementos do modelo cascata com a abordagem iterativa e o gerenciamento de riscos. Cada ciclo da espiral envolve planejamento, análise de risco, engenharia e avaliação do cliente. É adequado para projetos grandes e complexos com riscos significativos, pois o foco na análise de risco é contínuo.

*   **Modelo Incremental:** O software é construído e entregue em incrementos (partes) funcionais. Cada incremento adiciona novas funcionalidades ao sistema. O primeiro incremento geralmente contém as funcionalidades mais essenciais, e os incrementos subsequentes adicionam recursos adicionais. Permite que o cliente comece a usar o software mais cedo e forneça feedback.

*   **Metodologias Ágeis (Agile):** São um conjunto de abordagens de desenvolvimento de software que priorizam a entrega contínua de software funcional, a colaboração com o cliente, a adaptação a mudanças e a interação entre indivíduos, em vez de processos e ferramentas rígidos. O Manifesto Ágil (2001) define os princípios fundamentais. As metodologias ágeis mais populares incluem:
    *   **Scrum:** Um framework ágil que organiza o trabalho em ciclos curtos e iterativos chamados *sprints* (geralmente de 1 a 4 semanas). Possui papéis definidos (Product Owner, Scrum Master, Time de Desenvolvimento), artefatos (Product Backlog, Sprint Backlog, Incremento) e eventos (Planejamento da Sprint, Daily Scrum, Revisão da Sprint, Retrospectiva da Sprint).
    *   **Kanban:** Uma metodologia visual que foca na gestão do fluxo de trabalho. Utiliza um quadro Kanban (físico ou digital) para visualizar as tarefas em diferentes estágios (a fazer, em andamento, feito) e limitar o trabalho em progresso (WIP - Work In Progress) para otimizar o fluxo e reduzir gargalos.
    *   **XP (Extreme Programming):** Uma metodologia ágil que enfatiza práticas de engenharia de software, como programação em pares, desenvolvimento orientado a testes (TDD), integração contínua, refatoração e feedback constante do cliente.

#### Quarta-feira: Requisitos: levantamento (entrevistas, histórias de usuário), especificação (funcionais/não funcionais). Gerência de requisitos.

A fase de **requisitos** é uma das mais críticas no desenvolvimento de software, pois define o que o sistema deve fazer. Erros ou omissões nesta fase podem levar a grandes problemas e custos de correção nas etapas posteriores.

*   **Levantamento de Requisitos:** É o processo de descobrir, documentar e entender as necessidades dos usuários e as restrições do sistema. Técnicas comuns incluem:
    *   **Entrevistas:** Conversas diretas com stakeholders (usuários, gerentes, especialistas de domínio) para entender suas necessidades e expectativas.
    *   **Histórias de Usuário (User Stories):** Descrições curtas e simples de uma funcionalidade do sistema do ponto de vista do usuário, geralmente no formato: "Como um [tipo de usuário], eu quero [alguma meta] para que [algum motivo]". São amplamente usadas em metodologias ágeis.
    *   **Workshops:** Reuniões colaborativas com múltiplos stakeholders para discutir e definir requisitos.
    *   **Análise de Documentos:** Estudo de documentos existentes (manuais, relatórios, especificações de sistemas legados).
    *   **Observação:** Acompanhamento dos usuários em seu ambiente de trabalho para entender seus processos.

*   **Especificação de Requisitos:** É a documentação formal dos requisitos levantados. Os requisitos são geralmente classificados em:
    *   **Requisitos Funcionais:** Descrevem o que o sistema deve fazer. São as funcionalidades que o usuário espera do software (ex: "O sistema deve permitir que o usuário faça login", "O sistema deve gerar um relatório de vendas").
    *   **Requisitos Não Funcionais:** Descrevem como o sistema deve se comportar ou as qualidades que ele deve possuir. Incluem aspectos como desempenho (velocidade, tempo de resposta), segurança, usabilidade, confiabilidade, escalabilidade, manutenibilidade e portabilidade (ex: "O sistema deve responder em menos de 2 segundos", "O sistema deve ser seguro contra ataques de injeção SQL").

*   **Gerência de Requisitos:** É o processo de gerenciar as mudanças nos requisitos ao longo do ciclo de vida do projeto. Envolve atividades como:
    *   **Rastreabilidade:** Manter um registro de como cada requisito se relaciona com o projeto, o código e os testes.
    *   **Controle de Versão:** Gerenciar as diferentes versões dos documentos de requisitos.
    *   **Análise de Impacto:** Avaliar o impacto de uma mudança de requisito em outras partes do sistema e no cronograma/custo do projeto.
    *   **Priorização:** Classificar os requisitos com base em sua importância e urgência.

#### Quinta-feira: Design de software: arquitetura (monolítica, microsserviços, MVC), padrões de projeto (Strategy, Observer, Singleton). UML (diagrama de classes, sequência).

O **design de software** é a fase em que a estrutura e o comportamento do sistema são definidos, transformando os requisitos em um plano detalhado para a implementação. Envolve decisões sobre arquitetura, padrões e modelagem.

*   **Arquitetura de Software:** Descreve a estrutura geral do sistema, como seus componentes são organizados e como eles interagem. As arquiteturas comuns incluem:
    *   **Monolítica:** Todos os componentes do sistema (interface do usuário, lógica de negócios, acesso a dados) são empacotados em uma única unidade de implantação. É mais simples de desenvolver e implantar inicialmente, mas pode ser difícil de escalar e manter em projetos grandes.
    *   **Microsserviços:** O sistema é dividido em um conjunto de serviços pequenos, independentes e fracamente acoplados, cada um executando um processo único e se comunicando através de APIs. Oferece maior escalabilidade, resiliência e flexibilidade para usar diferentes tecnologias, mas adiciona complexidade de gerenciamento.
    *   **MVC (Model-View-Controller):** Um padrão arquitetural que separa a aplicação em três componentes principais:
        *   **Model:** Representa os dados e a lógica de negócios.
        *   **View:** Responsável pela apresentação dos dados ao usuário (interface).
        *   **Controller:** Gerencia a interação do usuário, recebendo entradas e atualizando o Model e a View.
        É amplamente utilizado em aplicações web e desktop para organizar o código e facilitar a manutenção.

*   **Padrões de Projeto (Design Patterns):** São soluções reutilizáveis para problemas comuns de design de software. Eles fornecem um vocabulário comum e uma forma estruturada de resolver problemas. Alguns exemplos:
    *   **Strategy:** Define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. Permite que o algoritmo varie independentemente dos clientes que o utilizam (ex: diferentes formas de calcular frete).
    *   **Observer:** Define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente (ex: sistema de notificação de eventos).
    *   **Singleton:** Garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a ela (ex: gerenciador de conexão de banco de dados).

*   **UML (Unified Modeling Language - Linguagem de Modelagem Unificada):** É uma linguagem gráfica padronizada para visualizar, especificar, construir e documentar os artefatos de um sistema de software. É amplamente utilizada para modelar sistemas orientados a objetos. Alguns diagramas comuns:
    *   **Diagrama de Classes:** Mostra a estrutura estática do sistema, representando classes, seus atributos, métodos e os relacionamentos entre elas (herança, associação, agregação, composição).
    *   **Diagrama de Sequência:** Mostra a interação entre objetos em uma ordem temporal. Ele ilustra como os objetos se comunicam entre si através de mensagens para realizar uma funcionalidade específica.
    *   Outros diagramas incluem diagrama de casos de uso, diagrama de atividades, diagrama de componentes, etc.

#### Sexta-feira: Testes e qualidade: pirâmide de testes (unitário, integração, sistema, aceitação). TDD, BDD. Métricas de software (coesão, acoplamento). DevOps e CI/CD.

A **qualidade do software** é um aspecto crucial que garante que o sistema atenda aos requisitos e funcione corretamente. Os **testes** são uma parte fundamental para assegurar essa qualidade.

*   **Pirâmide de Testes:** É um modelo que sugere a proporção ideal de diferentes tipos de testes em um projeto de software, com a base sendo os testes mais numerosos e rápidos, e o topo os menos numerosos e mais lentos:
    *   **Testes Unitários:** Testam as menores unidades de código (funções, métodos, classes) isoladamente. São rápidos, automatizados e numerosos. Foco em verificar a lógica interna do código.
    *   **Testes de Integração:** Verificam a interação entre diferentes módulos ou componentes do sistema. Garantem que as interfaces entre as unidades funcionem corretamente.
    *   **Testes de Sistema:** Testam o sistema completo como um todo, verificando se ele atende aos requisitos funcionais e não funcionais. Simulam o ambiente de produção.
    *   **Testes de Aceitação:** Realizados pelos usuários finais ou clientes para verificar se o sistema atende às suas expectativas e necessidades de negócio. Podem ser manuais ou automatizados.

*   **TDD (Test-Driven Development - Desenvolvimento Orientado a Testes):** É uma prática de desenvolvimento onde os testes são escritos *antes* do código de produção. O ciclo TDD é:
    1.  Escrever um teste que falha (porque a funcionalidade ainda não existe).
    2.  Escrever o código mínimo necessário para fazer o teste passar.
    3.  Refatorar o código (melhorar sua estrutura sem alterar seu comportamento) e garantir que todos os testes continuem passando.
    TDD ajuda a garantir a qualidade do código, a documentação através dos testes e a um design mais limpo.

*   **BDD (Behavior-Driven Development - Desenvolvimento Orientado a Comportamento):** É uma extensão do TDD que foca na colaboração entre desenvolvedores, testadores e stakeholders. Os requisitos são definidos em termos de comportamento esperado do sistema, usando uma linguagem natural (Gherkin) que pode ser entendida por todos. Ex: "Dado que [contexto], quando [ação], então [resultado esperado]". Os testes são escritos com base nessas descrições de comportamento.

*   **Métricas de Software:** São medidas quantitativas que ajudam a avaliar a qualidade e a complexidade do software. Duas métricas importantes são:
    *   **Coesão:** Mede o grau em que os elementos dentro de um módulo (classe, função) pertencem uns aos outros. Alta coesão significa que o módulo é focado em uma única responsabilidade, tornando-o mais fácil de entender, manter e reutilizar.
    *   **Acoplamento:** Mede o grau de dependência entre diferentes módulos. Baixo acoplamento significa que os módulos são independentes uns dos outros, o que facilita a modificação de um módulo sem afetar outros.

*   **DevOps e CI/CD:**
    *   **DevOps:** É uma cultura e um conjunto de práticas que visam integrar o desenvolvimento de software (Dev) e as operações de TI (Ops) para encurtar o ciclo de vida de desenvolvimento de sistemas e fornecer entrega contínua com alta qualidade. Enfatiza a automação, a comunicação e a colaboração.
    *   **CI/CD (Continuous Integration/Continuous Delivery ou Continuous Deployment):**
        *   **Integração Contínua (CI):** Prática de integrar as alterações de código de todos os desenvolvedores em um repositório central várias vezes ao dia. Cada integração é verificada por uma construção automatizada e testes para detectar erros rapidamente.
        *   **Entrega Contínua (CD):** Extensão da CI que garante que o software possa ser liberado para produção a qualquer momento. O código é construído, testado e preparado para implantação automaticamente.
        *   **Implantação Contínua (CD):** Uma etapa além da entrega contínua, onde cada alteração que passa por todos os estágios de teste é automaticamente implantada em produção.

---
### Semana 11 – Gerência de Projetos em TI

#### Segunda-feira: Conceitos de projeto, programa, portfólio. Ciclo de vida do projeto (iniciação, planejamento, execução, monitoramento, encerramento).

A **Gerência de Projetos** é a aplicação de conhecimentos, habilidades, ferramentas e técnicas às atividades do projeto para atender aos seus requisitos. Em TI, onde os projetos são frequentemente complexos e dinâmicos, uma boa gerência é crucial para o sucesso.

*   **Conceitos Fundamentais:**
    *   **Projeto:** Um esforço temporário empreendido para criar um produto, serviço ou resultado exclusivo. Possui um início e um fim definidos, e um objetivo específico. Ex: desenvolver um novo software, implementar uma nova rede.
    *   **Programa:** Um grupo de projetos relacionados, subprogramas e atividades de programa gerenciados de forma coordenada para obter benefícios que não estariam disponíveis se fossem gerenciados individualmente. Ex: um programa de transformação digital que inclui projetos de desenvolvimento de software, infraestrutura e treinamento.
    *   **Portfólio:** Uma coleção de projetos, programas, subportfólios e operações gerenciados como um grupo para atingir objetivos estratégicos de negócios. Ex: o portfólio de TI de uma empresa pode incluir projetos de inovação, manutenção e conformidade.

*   **Ciclo de Vida do Projeto:** Descreve as fases que um projeto passa desde o seu início até a sua conclusão. As fases típicas, conforme o PMBOK (Project Management Body of Knowledge), são:
    1.  **Iniciação:** Define o projeto, autoriza formalmente seu início e nomeia o gerente de projeto. É onde o termo de abertura do projeto (Project Charter) é criado, estabelecendo os objetivos iniciais e os stakeholders.
    2.  **Planejamento:** Detalha como o projeto será executado. Inclui a definição do escopo, cronograma, orçamento, recursos, riscos, qualidade, comunicações, aquisições e stakeholders. O plano de gerenciamento do projeto é o resultado principal desta fase.
    3.  **Execução:** Realiza o trabalho definido no plano de gerenciamento do projeto para atingir os objetivos. Envolve a coordenação de pessoas e recursos, a execução das atividades e a produção das entregas.
    4.  **Monitoramento e Controle:** Acompanha, revisa e regula o progresso do projeto para identificar desvios do plano e tomar ações corretivas. Garante que os objetivos de desempenho sejam atendidos.
    5.  **Encerramento:** Finaliza todas as atividades do projeto, formaliza a aceitação do produto, serviço ou resultado pelo cliente e encerra contratos. Inclui a lições aprendidas e a liberação da equipe.

#### Terça-feira: Estrutura analítica do projeto (EAP). Cronograma: diagrama de rede, PERT/CPM, caminho crítico. Uso do MS Project ou similares.

O **planejamento** é uma fase crucial na gerência de projetos, e ferramentas específicas são usadas para organizar e controlar o trabalho:

*   **Estrutura Analítica do Projeto (EAP - Work Breakdown Structure - WBS):** É uma decomposição hierárquica orientada às entregas do trabalho a ser executado pela equipe do projeto para atingir os objetivos do projeto e criar as entregas requeridas. A EAP organiza o escopo total do trabalho em componentes menores e mais gerenciáveis. Cada nível da EAP representa um detalhamento maior do trabalho, até chegar aos pacotes de trabalho, que são as menores unidades gerenciáveis.

*   **Cronograma do Projeto:** É uma representação gráfica ou tabular das atividades do projeto, suas durações, dependências e marcos. Ferramentas e técnicas para desenvolver e gerenciar o cronograma incluem:
    *   **Diagrama de Rede (Network Diagram):** Uma representação gráfica das atividades do projeto e suas dependências lógicas. Ajuda a visualizar a sequência das tarefas.
    *   **PERT (Program Evaluation and Review Technique) / CPM (Critical Path Method):** São técnicas de análise de rede que ajudam a estimar a duração do projeto e identificar o **caminho crítico**. O caminho crítico é a sequência de atividades que determina a duração total do projeto. Qualquer atraso em uma atividade do caminho crítico atrasará o projeto inteiro.
    *   **Gráfico de Gantt:** Uma representação visual do cronograma do projeto, mostrando as atividades em barras horizontais ao longo de uma linha do tempo. É amplamente utilizado para comunicar o progresso do projeto.

*   **Uso do MS Project ou Similares:** Ferramentas de software como Microsoft Project, Primavera P6, Asana, Jira ou Trello são utilizadas para criar, gerenciar e monitorar cronogramas de projetos, alocar recursos, acompanhar o progresso e gerar relatórios. Elas automatizam muitos dos cálculos e visualizações necessários para um planejamento eficaz.

#### Quarta-feira: Gerenciamento de riscos: identificação, análise qualitativa/quantitativa, plano de resposta. Matriz de probabilidade x impacto.

O **gerenciamento de riscos** é o processo de identificar, analisar e responder aos riscos do projeto. Um risco é um evento ou condição incerta que, se ocorrer, terá um efeito positivo ou negativo nos objetivos do projeto.

*   **Processos do Gerenciamento de Riscos:**
    1.  **Identificação de Riscos:** O processo de determinar quais riscos podem afetar o projeto e documentar suas características. Técnicas incluem brainstorming, análise SWOT, entrevistas, listas de verificação e análise de premissas.
    2.  **Análise Qualitativa de Riscos:** Avalia a probabilidade de ocorrência de um risco e o impacto potencial nos objetivos do projeto (custo, cronograma, escopo, qualidade). Os riscos são priorizados com base nessa avaliação.
    3.  **Análise Quantitativa de Riscos:** Realiza uma análise numérica do efeito de riscos identificados nos objetivos gerais do projeto. Usa técnicas como análise de Monte Carlo e análise de árvore de decisão para estimar a probabilidade de atingir os objetivos do projeto.
    4.  **Planejamento de Respostas a Riscos:** Desenvolve opções e ações para aumentar as oportunidades e reduzir as ameaças aos objetivos do projeto. As estratégias de resposta a riscos incluem:
        *   **Para Ameaças:** Evitar, Mitigar, Transferir, Aceitar.
        *   **Para Oportunidades:** Explorar, Melhorar, Compartilhar, Aceitar.
    5.  **Implementação de Respostas a Riscos:** Executa as ações planejadas para os riscos.
    6.  **Monitoramento de Riscos:** Acompanha os riscos identificados, monitora riscos residuais, identifica novos riscos e avalia a eficácia do plano de respostas a riscos.

*   **Matriz de Probabilidade x Impacto:** É uma ferramenta visual utilizada na análise qualitativa de riscos para priorizar os riscos. Ela plota a probabilidade de ocorrência de um risco contra o impacto que ele teria no projeto. Riscos com alta probabilidade e alto impacto são considerados de alta prioridade e exigem atenção imediata.

| Probabilidade \ Impacto | Baixo | Médio | Alto |
|-------------------------|-------|-------|------|
| Alta                    | Médio | Alto  | Crítico |
| Média                   | Baixo | Médio | Alto |
| Baixa                   | Baixo | Baixo | Médio |

#### Quinta-feira: Comunicação e stakeholders: matriz de responsabilidade (RACI), gestão de expectativas. Ferramentas (Trello, Jira, Asana).

A **comunicação** eficaz e a **gestão de stakeholders** são vitais para o sucesso de qualquer projeto. Stakeholders são indivíduos, grupos ou organizações que podem afetar, ser afetados ou se perceberem afetados por uma decisão, atividade ou resultado de um projeto.

*   **Comunicação no Projeto:** Envolve os processos necessários para garantir que as informações do projeto sejam planejadas, coletadas, criadas, distribuídas, armazenadas, recuperadas, gerenciadas, controladas, monitoradas e, finalmente, dispostas de forma oportuna e apropriada.

*   **Matriz de Responsabilidade (RACI):** É uma ferramenta utilizada para definir e documentar as funções e responsabilidades dos stakeholders em relação às atividades ou entregas do projeto. RACI é um acrônimo para:
    *   **Responsible (Responsável):** A pessoa que faz o trabalho para completar a tarefa. Há apenas um responsável por tarefa.
    *   **Accountable (Autoridade/Aprovador):** A pessoa que é, em última instância, responsável pela conclusão da tarefa ou entrega. Ela deve aprovar o trabalho do responsável. Há apenas um aprovador por tarefa.
    *   **Consulted (Consultado):** Pessoas que precisam ser consultadas antes que uma decisão ou ação seja tomada. A comunicação é bidirecional.
    *   **Informed (Informado):** Pessoas que precisam ser mantidas atualizadas sobre o progresso ou decisões. A comunicação é unidirecional.

*   **Gestão de Expectativas dos Stakeholders:** É o processo de comunicar e trabalhar com os stakeholders para atender às suas necessidades e expectativas, abordar questões à medida que surgem e fomentar o engajamento adequado. Envolve entender o que cada stakeholder espera do projeto e garantir que essas expectativas sejam realistas e alinhadas com os objetivos do projeto.

*   **Ferramentas de Gerenciamento de Projetos e Colaboração:**
    *   **Trello:** Uma ferramenta de gerenciamento de projetos baseada em quadros Kanban, ideal para equipes que buscam uma forma visual e flexível de organizar tarefas, acompanhar o progresso e colaborar. Usa cartões, listas e quadros.
    *   **Jira:** Uma ferramenta robusta e amplamente utilizada para gerenciamento de projetos ágeis (Scrum e Kanban), rastreamento de bugs e gerenciamento de problemas. Oferece funcionalidades avançadas para equipes de desenvolvimento de software.
    *   **Asana:** Uma ferramenta de gerenciamento de trabalho que ajuda as equipes a organizar, rastrear e gerenciar seus projetos. Oferece diferentes visualizações (lista, quadro, cronograma) e recursos de colaboração.

#### Sexta-feira: Metodologias ágeis para projetos: Scrum (papéis, artefatos, eventos), Planning Poker, Velocity. Certificações (CAPM, PMP, CSM).

As **metodologias ágeis** se tornaram predominantes na gerência de projetos de TI devido à sua flexibilidade e capacidade de adaptação a ambientes de mudança rápida. O **Scrum** é o framework ágil mais popular.

*   **Scrum:**
    *   **Papéis:**
        *   **Product Owner:** Representa os interesses dos stakeholders e do cliente. É responsável por maximizar o valor do produto e gerenciar o Product Backlog (lista priorizada de funcionalidades).
        *   **Scrum Master:** É um líder servidor que garante que a equipe Scrum siga os valores e práticas do Scrum. Remove impedimentos e facilita os eventos Scrum.
        *   **Time de Desenvolvimento:** Um grupo auto-organizado e multifuncional de profissionais que realiza o trabalho de entrega de um incremento de produto potencialmente utilizável a cada Sprint.
    *   **Artefatos:**
        *   **Product Backlog:** Uma lista ordenada e priorizada de tudo o que pode ser necessário no produto. É dinâmico e evolui com o projeto.
        *   **Sprint Backlog:** O conjunto de itens do Product Backlog selecionados para a Sprint atual, juntamente com o plano para entregá-los.
        *   **Incremento:** A soma de todos os itens do Product Backlog concluídos durante uma Sprint e o valor dos incrementos de todas as Sprints anteriores. Deve ser potencialmente utilizável.
    *   **Eventos (Cerimônias):**
        *   **Planejamento da Sprint (Sprint Planning):** Onde o Time de Desenvolvimento seleciona os itens do Product Backlog para a próxima Sprint e planeja como irá implementá-los.
        *   **Daily Scrum (Reunião Diária):** Uma reunião curta (15 minutos) diária para o Time de Desenvolvimento sincronizar atividades e planejar o trabalho das próximas 24 horas.
        *   **Revisão da Sprint (Sprint Review):** Uma reunião ao final da Sprint para inspecionar o Incremento e adaptar o Product Backlog, se necessário. O Time de Desenvolvimento demonstra o que foi feito.
        *   **Retrospectiva da Sprint (Sprint Retrospective):** Uma oportunidade para o Time Scrum inspecionar a si mesmo e criar um plano para melhorias a serem aplicadas na próxima Sprint.

*   **Planning Poker:** Uma técnica de estimativa baseada em consenso, usada em Scrum, onde os membros da equipe usam cartas numeradas (sequência de Fibonacci) para estimar o esforço ou a complexidade das histórias de usuário. Ajuda a obter estimativas mais precisas e a promover a discussão.

*   **Velocity (Velocidade):** Uma métrica em Scrum que mede a quantidade de trabalho (geralmente em pontos de história) que um Time de Desenvolvimento pode concluir em uma Sprint. É usada para prever o progresso futuro e planejar Sprints subsequentes.

*   **Certificações em Gerência de Projetos:**
    *   **CAPM (Certified Associate in Project Management):** Uma certificação de nível de entrada do PMI (Project Management Institute) para profissionais que desejam demonstrar seu compromisso com a gerência de projetos e sua compreensão dos fundamentos do PMBOK.
    *   **PMP (Project Management Professional):** A certificação mais reconhecida globalmente para gerentes de projeto experientes, também do PMI. Valida a experiência e a competência em liderar e dirigir projetos.
    *   **CSM (Certified ScrumMaster):** Uma certificação que valida o conhecimento e a compreensão do framework Scrum e o papel do Scrum Master. É oferecida pela Scrum Alliance.

---
### Semana 12 – Planejamento Estratégico e Empreendedorismo

#### Segunda-feira: Fundamentos do planejamento estratégico: missão, visão, valores. Análise SWOT (FOFA) pessoal e empresarial.

O **planejamento estratégico** é um processo fundamental para qualquer organização ou indivíduo que busca definir seu rumo e alcançar objetivos de longo prazo. Ele envolve a definição de onde se quer chegar e como se pretende fazer isso.

*   **Missão:** Declaração do propósito fundamental da organização ou indivíduo. Responde à pergunta: "Por que existimos?" Deve ser concisa, inspiradora e orientada para o presente. Ex: "Conectar pessoas e informações globalmente" (Google).

*   **Visão:** Descrição do futuro desejado para a organização ou indivíduo. Responde à pergunta: "Onde queremos chegar?" Deve ser ambiciosa, clara e orientada para o futuro. Ex: "Organizar as informações do mundo e torná-las universalmente acessíveis e úteis" (Google).

*   **Valores:** Princípios e crenças que guiam o comportamento e as decisões da organização ou indivíduo. Respondem à pergunta: "No que acreditamos?" Devem ser autênticos e refletir a cultura desejada. Ex: "Não seja mau" (antigo Google), "Foco no cliente", "Inovação".

*   **Análise SWOT (Strengths, Weaknesses, Opportunities, Threats) / FOFA (Forças, Oportunidades, Fraquezas, Ameaças):** É uma ferramenta de planejamento estratégico que ajuda a identificar os fatores internos e externos que podem afetar o sucesso de uma organização ou projeto. Pode ser aplicada tanto a empresas quanto a indivíduos (análise SWOT pessoal).
    *   **Forças (Strengths):** Fatores internos positivos que dão uma vantagem competitiva. Ex: equipe qualificada, tecnologia inovadora, forte reconhecimento de marca.
    *   **Fraquezas (Weaknesses):** Fatores internos negativos que podem prejudicar o desempenho. Ex: falta de recursos, processos ineficientes, dependência de um único cliente.
    *   **Oportunidades (Opportunities):** Fatores externos positivos que podem ser explorados para o benefício da organização. Ex: novo mercado, tecnologia emergente, mudança na legislação favorável.
    *   **Ameaças (Threats):** Fatores externos negativos que podem causar problemas. Ex: concorrência acirrada, crise econômica, novas regulamentações desfavoráveis.

#### Terça-feira: Estratégias competitivas (Porter: 5 forças, estratégias genéricas). BSC (Balanced Scorecard) e OKRs.

Para ter sucesso no mercado, as organizações precisam desenvolver **estratégias competitivas** eficazes. Michael Porter, um renomado estrategista, propôs modelos influentes:

*   **As Cinco Forças de Porter:** Uma estrutura para analisar a atratividade de uma indústria e a intensidade da concorrência. As cinco forças são:
    1.  **Ameaça de Novos Entrantes:** Quão fácil é para novas empresas entrarem no mercado.
    2.  **Poder de Barganha dos Compradores:** A capacidade dos clientes de pressionar por preços mais baixos ou maior qualidade.
    3.  **Poder de Barganha dos Fornecedores:** A capacidade dos fornecedores de aumentar preços ou reduzir a qualidade.
    4.  **Ameaça de Produtos Substitutos:** A probabilidade de os clientes encontrarem alternativas para o produto ou serviço.
    5.  **Rivalidade entre Concorrentes Existentes:** A intensidade da concorrência entre as empresas já estabelecidas na indústria.

*   **Estratégias Genéricas de Porter:** Três abordagens fundamentais para alcançar vantagem competitiva:
    1.  **Liderança em Custo:** Ser o produtor de menor custo na indústria, oferecendo produtos ou serviços a preços mais baixos que os concorrentes. Ex: companhias aéreas de baixo custo.
    2.  **Diferenciação:** Oferecer produtos ou serviços únicos e de alto valor percebido pelos clientes, que estão dispostos a pagar um preço premium por eles. Ex: marcas de luxo, Apple.
    3.  **Foco:** Concentrar-se em um nicho de mercado específico (seja por custo ou diferenciação), atendendo às necessidades desse segmento de forma mais eficaz do que os concorrentes que atuam em um mercado mais amplo.

*   **BSC (Balanced Scorecard):** É uma metodologia de gestão estratégica que traduz a missão e a visão de uma organização em um conjunto abrangente de medidas de desempenho. Ele equilibra indicadores financeiros com indicadores não financeiros, organizados em quatro perspectivas:
    1.  **Financeira:** Como a empresa é vista pelos acionistas (lucratividade, crescimento).
    2.  **Clientes:** Como a empresa é vista pelos clientes (satisfação, retenção).
    3.  **Processos Internos:** No que a empresa deve ser excelente (eficiência operacional, qualidade).
    4.  **Aprendizado e Crescimento:** Como a empresa pode continuar a melhorar e criar valor (inovação, capacitação de funcionários).

*   **OKRs (Objectives and Key Results - Objetivos e Resultados-Chave):** É uma metodologia de definição e acompanhamento de metas que ajuda a alinhar e engajar equipes em torno de objetivos ambiciosos e mensuráveis. Um **Objetivo** é o que se quer alcançar (inspirador, qualitativo). Um **Resultado-Chave** é como se mede o progresso e a conclusão do objetivo (específico, mensurável, atingível, relevante, temporal). Ex: Objetivo: "Lançar um produto incrível". KR1: "Atingir 1 milhão de usuários ativos". KR2: "Obter 4.5 estrelas de avaliação na loja de aplicativos".

#### Quarta-feira: Empreendedorismo em TI: identificação de oportunidades, canvas do modelo de negócios (BMC). Product Market Fit.

O **empreendedorismo em TI** envolve a criação e o desenvolvimento de novos negócios ou projetos inovadores no setor de tecnologia. Para ter sucesso, é crucial identificar oportunidades e estruturar um modelo de negócios sólido.

*   **Identificação de Oportunidades:** Empreendedores de TI buscam resolver problemas existentes ou atender a necessidades não satisfeitas no mercado. Isso pode envolver:
    *   **Observação:** Identificar dores e frustrações de usuários ou empresas.
    *   **Tendências Tecnológicas:** Aproveitar o surgimento de novas tecnologias (IA, blockchain, IoT) para criar soluções inovadoras.
    *   **Análise de Mercado:** Pesquisar lacunas em produtos ou serviços existentes.
    *   **Networking:** Conversar com pessoas da indústria e potenciais clientes.
    *   **Paixão e Conhecimento:** Transformar um interesse pessoal ou expertise em uma solução de negócio.

*   **Canvas do Modelo de Negócios (Business Model Canvas - BMC):** É uma ferramenta visual estratégica para descrever, projetar, inventar e inovar modelos de negócios. Ele é composto por nove blocos interconectados que cobrem os aspectos mais importantes de um negócio:
    1.  **Segmentos de Clientes:** Para quem estamos criando valor?
    2.  **Proposições de Valor:** Que valor entregamos aos clientes? Que problema estamos resolvendo?
    3.  **Canais:** Como entregamos a proposição de valor aos clientes?
    4.  **Relacionamento com Clientes:** Que tipo de relacionamento estabelecemos com cada segmento de clientes?
    5.  **Fontes de Receita:** Como geramos receita a partir da proposição de valor?
    6.  **Recursos Principais:** Que recursos são necessários para entregar a proposição de valor?
    7.  **Atividades Principais:** Que atividades são cruciais para operar o modelo de negócios?
    8.  **Parcerias Principais:** Quem são nossos parceiros e fornecedores chave?
    9.  **Estrutura de Custos:** Quais são os custos mais importantes inerentes ao modelo de negócios?

*   **Product Market Fit (PMF):** É o grau em que um produto satisfaz uma forte demanda do mercado. Atingir o PMF significa que você encontrou um bom mercado com um produto que pode satisfazer esse mercado. É um marco crucial para startups, pois indica que o produto tem potencial para crescer e ser bem-sucedido. Sem PMF, é muito difícil escalar um negócio, mesmo com um bom produto.

#### Quinta-feira: Lean Startup (MVP, ciclo Construir-Medir-Aprender). Métricas para startups (ARR, MRR, Churn, CAC, LTV).

A metodologia **Lean Startup**, popularizada por Eric Ries, oferece uma abordagem científica para a criação e gestão de startups, enfatizando a experimentação, o feedback do cliente e o desenvolvimento iterativo.

*   **MVP (Minimum Viable Product - Produto Mínimo Viável):** É a versão de um novo produto que permite à equipe coletar a quantidade máxima de aprendizado validado sobre os clientes com o mínimo esforço. O MVP não é um produto incompleto, mas sim a versão mais simples que ainda entrega valor e permite testar as hipóteses mais críticas do negócio. O objetivo é lançar rapidamente, aprender e iterar.

*   **Ciclo Construir-Medir-Aprender:** O coração da metodologia Lean Startup. É um ciclo contínuo de feedback:
    1.  **Construir (Build):** Desenvolver um MVP ou uma nova funcionalidade com base em uma hipótese.
    2.  **Medir (Measure):** Coletar dados e métricas sobre como os usuários interagem com o MVP ou a funcionalidade.
    3.  **Aprender (Learn):** Analisar os dados para validar ou invalidar as hipóteses. Com base no aprendizado, decidir se é preciso **pivotar** (mudar a estratégia) ou **perseverar** (continuar na mesma direção com ajustes).

*   **Métricas Essenciais para Startups (SaaS - Software as a Service):**
    *   **ARR (Annual Recurring Revenue - Receita Recorrente Anual):** A receita total que uma empresa espera gerar de seus clientes em um ano, com base em assinaturas ou contratos recorrentes. É uma métrica chave para avaliar o crescimento e a saúde financeira de empresas SaaS.
    *   **MRR (Monthly Recurring Revenue - Receita Recorrente Mensal):** A receita total que uma empresa espera gerar de seus clientes em um mês, com base em assinaturas ou contratos recorrentes. É o ARR dividido por 12.
    *   **Churn Rate (Taxa de Churn):** A porcentagem de clientes que cancelam suas assinaturas ou deixam de usar o serviço em um determinado período. Uma alta taxa de churn é prejudicial para o crescimento e a lucratividade.
    *   **CAC (Customer Acquisition Cost - Custo de Aquisição de Cliente):** O custo total de marketing e vendas necessário para adquirir um novo cliente. É calculado dividindo o total de gastos em marketing e vendas pelo número de novos clientes adquiridos.
    *   **LTV (Lifetime Value - Valor do Tempo de Vida do Cliente):** A receita total que uma empresa espera gerar de um cliente ao longo de todo o seu relacionamento. Para um negócio sustentável, o LTV deve ser significativamente maior que o CAC.

#### Sexta-feira: Finanças para empreendedores: fluxo de caixa, ponto de equilíbrio, valuation básico. Captação de recursos (bootstrapping, investidor-anjo, venture capital).

Para o empreendedor de TI, entender os fundamentos de **finanças** é tão importante quanto a tecnologia em si. Uma boa gestão financeira é crucial para a sustentabilidade e o crescimento do negócio.

*   **Fluxo de Caixa:** É o movimento de dinheiro que entra (receitas) e sai (despesas) de uma empresa em um determinado período. Monitorar o fluxo de caixa é vital para garantir que a empresa tenha dinheiro suficiente para cobrir suas operações diárias e investir no crescimento. Um fluxo de caixa positivo indica que a empresa está gerando mais dinheiro do que gasta.

*   **Ponto de Equilíbrio (Break-even Point):** É o nível de vendas (em unidades ou em valor monetário) no qual a receita total de uma empresa é igual aos seus custos totais (fixos e variáveis). No ponto de equilíbrio, a empresa não tem lucro nem prejuízo. É uma métrica importante para determinar a viabilidade de um negócio e definir metas de vendas mínimas.

*   **Valuation Básico:** É o processo de estimar o valor econômico de uma empresa ou ativo. Para startups, o valuation é crucial para atrair investidores e determinar a participação acionária que eles receberão em troca de investimento. Métodos básicos incluem:
    *   **Múltiplos de Mercado:** Comparar a startup com empresas semelhantes que já foram avaliadas ou vendidas.
    *   **Fluxo de Caixa Descontado (DCF):** Projetar os fluxos de caixa futuros da empresa e descontá-los para o valor presente.
    *   **Método de Venture Capital:** Estimar o valor futuro da empresa e descontá-lo, considerando a participação desejada pelo investidor.

*   **Captação de Recursos:** As startups frequentemente precisam de capital externo para financiar seu crescimento. As principais formas de captação incluem:
    *   **Bootstrapping:** Financiar o negócio com recursos próprios ou com a receita gerada pelo próprio negócio, sem depender de investidores externos. Permite maior controle, mas limita o crescimento rápido.
    *   **Investidor-Anjo (Angel Investor):** Indivíduos de alto patrimônio líquido que investem seu próprio dinheiro em startups em estágio inicial, geralmente em troca de participação acionária. Além do capital, oferecem mentoria e experiência.
    *   **Venture Capital (Capital de Risco):** Fundos de investimento que aplicam capital em startups com alto potencial de crescimento, em troca de participação acionária significativa. Geralmente investem em estágios mais avançados do que os investidores-anjo e buscam um retorno substancial em poucos anos.
    *   **Crowdfunding:** Arrecadação de fundos de um grande número de pessoas, geralmente pela internet, em troca de recompensas, participação acionária ou dívida.

---
### Semana 13 – Segurança do Trabalho e Sistemas Operacionais II

#### Segunda-feira: Segurança do trabalho em TI: ergonomia (postura, iluminação, pausas ativas). NR17 e NR12 aplicadas a laboratórios.

A **segurança do trabalho em TI** é fundamental para garantir a saúde e o bem-estar dos profissionais, prevenindo acidentes e doenças ocupacionais. Em ambientes de TI, as preocupações se estendem desde a ergonomia até os riscos elétricos.

*   **Ergonomia:** É a ciência que estuda a relação entre o homem e seu ambiente de trabalho, buscando otimizar o bem-estar e o desempenho. Em TI, a ergonomia é crucial para prevenir lesões por esforço repetitivo (LER) e distúrbios osteomusculares relacionados ao trabalho (DORT).
    *   **Postura:** Manter uma postura correta ao sentar, com a coluna ereta, pés apoiados no chão, cotovelos em ângulo de 90 graus e punhos retos em relação ao teclado e mouse. A cadeira deve ser ergonômica, com ajustes de altura e apoio lombar.
    *   **Iluminação:** A iluminação do ambiente de trabalho deve ser adequada, evitando reflexos na tela do computador e garantindo que não haja ofuscamento. A luz natural é preferível, complementada por iluminação artificial difusa.
    *   **Pausas Ativas:** Realizar pequenas pausas regulares (a cada 50 minutos de trabalho, por exemplo) para levantar, alongar-se e descansar os olhos. Isso ajuda a reduzir a fadiga física e mental.

*   **Normas Regulamentadoras (NRs) Aplicadas a Laboratórios de TI:** As NRs são disposições complementares à CLT (Consolidação das Leis do Trabalho) que estabelecem requisitos e procedimentos relativos à segurança e saúde no trabalho.
    *   **NR 17 (Ergonomia):** Estabelece parâmetros que permitam a adaptação das condições de trabalho às características psicofisiológicas dos trabalhadores, de modo a proporcionar o máximo de conforto, segurança e desempenho eficiente. É diretamente aplicável à configuração de estações de trabalho em TI.
    *   **NR 12 (Segurança no Trabalho em Máquinas e Equipamentos):** Embora mais focada em máquinas industriais, seus princípios de segurança na operação e manutenção de equipamentos são relevantes para laboratórios de TI que lidam com montagem, manutenção e testes de hardware, especialmente em relação a partes móveis, riscos de choque elétrico e manuseio seguro.

#### Terça-feira: Riscos elétricos e incêndio: aterramento, DR, no-break, estabilizador. Normas NR10. Uso de EPI/EPC.

Os **riscos elétricos e de incêndio** são preocupações sérias em qualquer ambiente com equipamentos eletrônicos, incluindo laboratórios e escritórios de TI. A prevenção é essencial.

*   **Riscos Elétricos:**
    *   **Aterramento:** É a conexão de equipamentos elétricos à terra, fornecendo um caminho de baixa resistência para a corrente elétrica em caso de falha. O aterramento protege contra choques elétricos e garante o funcionamento correto dos dispositivos.
    *   **DR (Dispositivo Diferencial Residual):** Um dispositivo de segurança que detecta pequenas fugas de corrente elétrica (que podem causar choques) e desliga o circuito rapidamente, protegendo as pessoas. É obrigatório em muitas instalações.
    *   **No-break (UPS - Uninterruptible Power Supply):** Um equipamento que fornece energia elétrica ininterrupta aos dispositivos conectados em caso de queda ou flutuação da rede elétrica. Protege contra perda de dados e danos a equipamentos sensíveis.
    *   **Estabilizador:** Um dispositivo que regula a tensão da rede elétrica, protegendo os equipamentos contra variações de voltagem. Embora menos comum em ambientes modernos (fontes de PC já são bivolt e com PFC ativo), ainda pode ser encontrado.

*   **Norma Regulamentadora NR 10 (Segurança em Instalações e Serviços em Eletricidade):** Estabelece os requisitos e condições mínimas para garantir a segurança e a saúde dos trabalhadores que interagem com instalações e serviços em eletricidade. É crucial para profissionais de TI que lidam com infraestrutura de rede, servidores e manutenção de hardware, exigindo capacitação específica.

*   **Uso de EPI/EPC:**
    *   **EPI (Equipamento de Proteção Individual):** Dispositivos ou produtos de uso individual utilizados pelo trabalhador para protegê-lo de riscos que possam ameaçar sua segurança e saúde. Em TI, pode incluir luvas isolantes (para manuseio de componentes elétricos), óculos de segurança (em laboratórios de solda), calçados de segurança.
    *   **EPC (Equipamento de Proteção Coletiva):** Dispositivos instalados no ambiente de trabalho para proteger coletivamente os trabalhadores. Exemplos incluem extintores de incêndio, sinalização de segurança, sistemas de ventilação, mantas isolantes, barreiras de proteção.

#### Quarta-feira: Segurança da informação e trabalho: política de senhas, backup, descarte seguro de mídias. LGPD no ambiente corporativo.

A **segurança da informação** é um pilar fundamental em qualquer organização, especialmente na era digital. Ela visa proteger os dados contra acesso não autorizado, uso, divulgação, interrupção, modificação ou destruição.

*   **Política de Senhas:** Um conjunto de regras e diretrizes que os usuários devem seguir ao criar e gerenciar suas senhas. Uma boa política de senhas inclui:
    *   **Complexidade:** Exigir senhas longas, com combinação de letras maiúsculas e minúsculas, números e caracteres especiais.
    *   **Periodicidade:** Recomendar a troca regular de senhas (embora a tendência atual seja focar mais na complexidade e no uso de autenticação de dois fatores).
    *   **Exclusividade:** Proibir o uso da mesma senha para diferentes serviços.
    *   **Armazenamento Seguro:** Orientar sobre o uso de gerenciadores de senhas e a proibição de anotar senhas em locais visíveis.

*   **Backup:** É a cópia de dados importantes para um local seguro, a fim de protegê-los contra perda devido a falhas de hardware, erros humanos, ataques cibernéticos ou desastres. Uma estratégia de backup eficaz envolve:
    *   **Regularidade:** Realizar backups de forma consistente e programada.
    *   **Localização:** Armazenar cópias em locais diferentes (regra 3-2-1: 3 cópias, em 2 mídias diferentes, 1 cópia off-site).
    *   **Testes:** Verificar periodicamente a integridade dos backups e a capacidade de restauração.

*   **Descarte Seguro de Mídias:** A simples exclusão de arquivos ou formatação de um disco não garante que os dados sejam irrecuperáveis. O descarte seguro de mídias (HDDs, SSDs, pendrives, CDs/DVDs) é crucial para evitar vazamento de informações sensíveis. Métodos incluem:
    *   **Sobregravação:** Escrever dados aleatórios múltiplas vezes sobre os dados originais.
    *   **Desmagnetização (Degaussing):** Usar um campo magnético forte para apagar dados de mídias magnéticas (HDDs).
    *   **Destruição Física:** Trituração, incineração ou perfuração da mídia.

*   **LGPD (Lei Geral de Proteção de Dados) no Ambiente Corporativo:** A LGPD (Lei nº 13.709/2018) estabelece regras sobre coleta, armazenamento, tratamento e compartilhamento de dados pessoais, visando proteger a privacidade e os direitos dos titulares dos dados. No ambiente corporativo, as empresas devem:
    *   **Obter Consentimento:** Coletar dados pessoais apenas com o consentimento explícito do titular ou com base em outra base legal.
    *   **Garantir a Segurança:** Implementar medidas técnicas e administrativas para proteger os dados contra acessos não autorizados e incidentes.
    *   **Transparência:** Informar aos titulares sobre como seus dados são coletados, usados e armazenados.
    *   **Direitos dos Titulares:** Respeitar os direitos dos indivíduos, como acesso, correção, exclusão e portabilidade de seus dados.
    *   **Encarregado de Dados (DPO):** Nomear um responsável pela proteção de dados.

#### Quinta-feira: Sistemas Operacionais II: virtualização (Hyper-V, VMware, VirtualBox). Containers (Docker) – criação, gerenciamento, orquestração (Kubernetes conceitos).

Continuando o estudo dos Sistemas Operacionais, esta aula aprofunda em tecnologias modernas que otimizam o uso de recursos e facilitam o desenvolvimento e a implantação de aplicações.

*   **Virtualização:** É a criação de uma versão virtual (e não física) de algo, como um sistema operacional, um servidor, um dispositivo de armazenamento ou recursos de rede. Permite executar múltiplos sistemas operacionais em um único hardware físico.
    *   **Hypervisor (Monitor de Máquina Virtual - VMM):** É o software que cria e executa máquinas virtuais (VMs). Ele gerencia o hardware físico e aloca recursos para cada VM.
        *   **Tipo 1 (Bare-metal):** O hypervisor é instalado diretamente no hardware físico, sem um sistema operacional hospedeiro. Oferece melhor desempenho e segurança. Ex: VMware ESXi, Microsoft Hyper-V, Xen.
        *   **Tipo 2 (Hosted):** O hypervisor é instalado sobre um sistema operacional hospedeiro. Mais fácil de usar para testes e desenvolvimento. Ex: Oracle VirtualBox, VMware Workstation, Parallels Desktop.
    *   **Vantagens da Virtualização:** Consolidação de servidores (redução de custos de hardware e energia), isolamento de aplicações, alta disponibilidade, recuperação de desastres, flexibilidade e portabilidade.

*   **Containers (Docker):** Uma tecnologia de virtualização mais leve e eficiente que as máquinas virtuais. Em vez de virtualizar o hardware, os containers virtualizam o sistema operacional. Eles empacotam uma aplicação e todas as suas dependências (bibliotecas, configurações) em uma unidade isolada, garantindo que ela funcione de forma consistente em qualquer ambiente.
    *   **Docker:** É a plataforma mais popular para criar, implantar e gerenciar containers. Ele usa o conceito de imagens (templates de containers) e containers (instâncias em execução das imagens).
        *   **Criação de Containers:** Definir um `Dockerfile` que especifica as etapas para construir uma imagem (ex: sistema operacional base, instalação de dependências, cópia do código da aplicação).
        *   **Gerenciamento de Containers:** Comandos Docker para iniciar, parar, remover, listar containers e imagens.

*   **Orquestração de Containers (Kubernetes Conceitos):** À medida que o número de containers cresce, gerenciá-los manualmente se torna inviável. Ferramentas de orquestração automatizam a implantação, escalonamento, gerenciamento e rede de containers.
    *   **Kubernetes (K8s):** É a plataforma de orquestração de containers de código aberto mais amplamente adotada. Ele automatiza a implantação, o escalonamento e o gerenciamento de aplicações em containers. Conceitos chave incluem:
        *   **Pods:** A menor unidade implantável no Kubernetes, que encapsula um ou mais containers.
        *   **Deployments:** Gerenciam o estado desejado dos Pods, garantindo que um número específico de réplicas esteja sempre em execução.
        *   **Services:** Abstraem a rede dos Pods, fornecendo um ponto de acesso estável para as aplicações.
        *   **Nodes:** As máquinas (físicas ou virtuais) onde os Pods são executados.
        *   **Cluster:** Um conjunto de Nodes gerenciados pelo Kubernetes.

#### Sexta-feira: SOs avançados: Linux (comandos essenciais, permissões, shell script). Windows Server (Active Directory, GPO). Introdução a SOs de tempo real (RTOS).

Esta aula explora aspectos mais avançados de sistemas operacionais, focando em sistemas amplamente utilizados em servidores e em aplicações específicas.

*   **Linux:** Um sistema operacional de código aberto, robusto e flexível, amplamente utilizado em servidores, sistemas embarcados e supercomputadores. É conhecido por sua estabilidade, segurança e capacidade de personalização.
    *   **Comandos Essenciais:**
        *   `ls`: Lista o conteúdo de um diretório.
        *   `cd`: Muda de diretório.
        *   `pwd`: Mostra o diretório de trabalho atual.
        *   `mkdir`: Cria um diretório.
        *   `rm`: Remove arquivos ou diretórios.
        *   `cp`: Copia arquivos ou diretórios.
        *   `mv`: Move ou renomeia arquivos ou diretórios.
        *   `cat`: Exibe o conteúdo de um arquivo.
        *   `grep`: Procura por padrões em arquivos.
        *   `chmod`: Altera permissões de arquivos.
        *   `chown`: Altera o proprietário de arquivos.
        *   `sudo`: Executa comandos como superusuário.
        *   `apt` / `yum`: Gerenciadores de pacotes para instalar software.
    *   **Permissões de Arquivo:** No Linux, as permissões são definidas para o proprietário (user), o grupo (group) e outros (others), com três tipos de acesso: leitura (r), escrita (w) e execução (x). Podem ser representadas por letras (rwx) ou números octais (ex: `755` para `rwxr-xr-x`).
    *   **Shell Script:** Programas escritos para serem executados por um interpretador de comandos (shell), como Bash. Permitem automatizar tarefas repetitivas, gerenciar o sistema e criar ferramentas personalizadas. São fundamentais para a administração de sistemas Linux.

*   **Windows Server:** A versão do sistema operacional Windows projetada para ambientes de servidor, oferecendo recursos e serviços para gerenciar redes, usuários e aplicações em escala corporativa.
    *   **Active Directory (AD):** Um serviço de diretório da Microsoft que armazena informações sobre objetos de rede (usuários, computadores, impressoras, serviços) e fornece serviços de autenticação e autorização. É a espinha dorsal da maioria das redes Windows corporativas.
    *   **GPO (Group Policy Object - Objeto de Política de Grupo):** Um recurso do Active Directory que permite aos administradores aplicar configurações de segurança, software e comportamento a usuários e computadores em uma rede. Facilita a padronização e o gerenciamento centralizado de ambientes Windows.

*   **Introdução a SOs de Tempo Real (RTOS - Real-Time Operating Systems):** São sistemas operacionais projetados para processar dados com restrições de tempo rigorosas, garantindo que as operações sejam concluídas dentro de prazos definidos. São usados em aplicações críticas onde atrasos podem ter consequências graves.
    *   **Características:** Determinismo (previsibilidade do tempo de resposta), baixa latência, alta confiabilidade.
    *   **Aplicações:** Controle industrial, sistemas embarcados automotivos, equipamentos médicos, sistemas de aviação e defesa.
    *   **Exemplos:** FreeRTOS, VxWorks, QNX.

---
### Semana 14 – Revisão e Projeto Integrador Transversal

#### Segunda-feira: Revisão do Módulo II (quiz + desafios práticos: calcular resistor, desenhar um CLP, montar backlog Scrum).

Este dia é dedicado à revisão e consolidação dos conhecimentos adquiridos no Módulo II, que abrange **Gerência, Automação e Eletrônica**. A revisão será feita através de um quiz e desafios práticos para aplicar os conceitos de forma mais concreta.

**Quiz de Revisão:**

*   **Automação:** O que é automação e quais seus principais componentes (sensores, atuadores, controladores)? Diferencie sensores indutivos, capacitivos e ópticos. Explique o funcionamento de um CLP e suas linguagens de programação (Ladder, FBD, ST). O que são SCADA, Modbus e Profibus? Quais os pilares da Indústria 4.0 e o que é IIoT e Gêmeos Digitais?
*   **Eletrônica:** Defina tensão, corrente, resistência e potência. Explique a Lei de Ohm. Qual a diferença entre circuitos série e paralelo? Cite exemplos de componentes passivos (resistor, capacitor, indutor) e ativos (diodo, transistor). Como funciona um CI 555 e um amplificador operacional? O que é PWM e como ele controla atuadores?
*   **Engenharia de Software:** Qual a diferença entre programação e engenharia de software? Descreva o ciclo de vida cascata. Quais as características dos modelos iterativo, espiral e incremental? Explique os conceitos de Scrum, Kanban e XP. Qual a importância dos requisitos funcionais e não funcionais? O que são arquiteturas monolítica e de microsserviços? Cite exemplos de padrões de projeto. Explique a pirâmide de testes e o que são TDD e BDD. O que é DevOps e CI/CD?
*   **Gerência de Projetos:** Defina projeto, programa e portfólio. Quais as fases do ciclo de vida do projeto? O que é EAP e caminho crítico? Como funciona o gerenciamento de riscos? Explique a matriz RACI. Quais os papéis, artefatos e eventos do Scrum? O que são Planning Poker e Velocity?
*   **Planejamento Estratégico e Empreendedorismo:** Qual a diferença entre missão, visão e valores? Explique a análise SWOT. Quais as 5 forças e as estratégias genéricas de Porter? O que são BSC e OKRs? Como identificar oportunidades em TI? O que é o Canvas do Modelo de Negócios? Explique MVP e o ciclo Construir-Medir-Aprender. Quais as métricas importantes para startups (ARR, MRR, Churn, CAC, LTV)? Quais as formas de captação de recursos?
*   **Segurança do Trabalho e SO II:** Quais os princípios de ergonomia em TI? O que são NR17 e NR12? Quais os riscos elétricos e como preveni-los (aterramento, DR, no-break)? O que é NR10? Qual a importância da política de senhas, backup e descarte seguro de mídias? Como a LGPD se aplica no ambiente corporativo? Explique virtualização (Hyper-V, VMware, VirtualBox) e containers (Docker). Quais os conceitos de orquestração com Kubernetes? Cite comandos essenciais do Linux e explique Active Directory e GPO no Windows Server. O que são RTOS?

**Desafios Práticos:**

*   **Calcular Resistor:** Dado um LED e uma fonte de tensão, calcular o valor do resistor limitador de corrente necessário. (Ex: LED com Vf=2V, If=20mA, fonte de 5V. R = (5-2)/0.02 = 150 Ohms).
*   **Desenhar um Circuito CLP Simples:** Desenhar um diagrama Ladder para controlar um motor que liga com um botão e desliga com outro, com um temporizador que o desliga automaticamente após 10 segundos.
*   **Montar um Backlog Scrum:** Criar um Product Backlog inicial para um projeto fictício (ex: um aplicativo de lista de tarefas), com algumas histórias de usuário priorizadas.

#### Terça-feira: Início do Projeto Integrador: definição de tema (ex: sistema de automação residencial + dashboard web).

Este dia marca o início do **Projeto Integrador**, que tem como objetivo aplicar de forma prática e conjunta os conhecimentos adquiridos nos Módulos I e II. A primeira etapa é a **definição do tema** e do escopo geral do projeto.

*   **Propósito do Projeto Integrador:**
    *   Sintetizar e aplicar os conceitos de hardware, redes, sistemas operacionais, eletrônica, automação, engenharia de software e gerência de projetos.
    *   Desenvolver habilidades de resolução de problemas e trabalho em equipe (mesmo que simulado).
    *   Criar um produto ou solução que demonstre a capacidade de integrar diferentes áreas da TI.

*   **Sugestão de Tema:** Um **sistema de automação residencial com um dashboard web** é um excelente tema, pois permite integrar diversas áreas:
    *   **Hardware:** Sensores (temperatura, luz, presença), atuadores (LEDs, relés para lâmpadas, motores para cortinas).
    *   **Eletrônica:** Conexão dos sensores e atuadores a um microcontrolador (ex: Arduino, Raspberry Pi).
    *   **Automação:** Lógica de controle para acionar dispositivos com base em leituras de sensores ou comandos do usuário.
    *   **Redes:** Conectividade do microcontrolador à rede local e à internet.
    *   **Sistemas Operacionais:** Uso de um SO embarcado (no Raspberry Pi) ou a programação do microcontrolador.
    *   **Engenharia de Software:** Desenvolvimento do firmware do microcontrolador e do dashboard web.
    *   **Gerência de Projetos:** Planejamento, execução e monitoramento do projeto.

*   **Outras Sugestões de Temas (alternativas):**
    *   Sistema de monitoramento de estufa agrícola com controle de irrigação.
    *   Estação meteorológica com envio de dados para a nuvem.
    *   Robô seguidor de linha com controle via aplicativo móvel.

*   **Primeiros Passos:**
    *   Brainstorming para refinar a ideia e definir funcionalidades básicas.
    *   Esboçar os principais componentes do sistema (hardware e software).
    *   Definir os objetivos claros e mensuráveis para o projeto.

#### Quarta-feira: Aplicando engenharia de software e gerência de projetos ao projeto (requisitos, EAP, riscos).

Com o tema do Projeto Integrador definido, o foco agora é aplicar as metodologias de **engenharia de software** e **gerência de projetos** para estruturar o trabalho. Esta etapa é crucial para garantir que o projeto seja desenvolvido de forma organizada e eficiente.

*   **Levantamento e Especificação de Requisitos (Engenharia de Software):**
    *   **Requisitos Funcionais:** O que o sistema de automação residencial deve fazer? (Ex: "O sistema deve ligar/desligar lâmpadas via dashboard", "O sistema deve monitorar a temperatura ambiente", "O sistema deve acionar um alarme em caso de detecção de movimento").
    *   **Requisitos Não Funcionais:** Como o sistema deve se comportar? (Ex: "O dashboard deve ser responsivo", "O sistema deve ter um tempo de resposta inferior a 500ms", "O sistema deve ser seguro contra acessos não autorizados").
    *   **Histórias de Usuário:** Criar histórias de usuário para as funcionalidades principais (Ex: "Como morador, quero ligar a luz da sala pelo celular para ter comodidade").

*   **Estrutura Analítica do Projeto (EAP - Gerência de Projetos):** Decompor o projeto em entregas menores e mais gerenciáveis. Exemplo de EAP para o sistema de automação residencial:
    *   **Projeto Automação Residencial**
        *   **1. Gerência do Projeto**
            *   1.1. Planejamento
            *   1.2. Monitoramento e Controle
            *   1.3. Encerramento
        *   **2. Hardware**
            *   2.1. Seleção de Componentes (microcontrolador, sensores, atuadores)
            *   2.2. Montagem e Teste de Circuitos
            *   2.3. Integração Hardware-Software
        *   **3. Software Embarcado (Firmware)**
            *   3.1. Desenvolvimento da Lógica de Controle
            *   3.2. Comunicação com Sensores/Atuadores
            *   3.3. Comunicação de Rede
        *   **4. Dashboard Web**
            *   4.1. Design UX/UI (Figma)
            *   4.2. Desenvolvimento Front-end (HTML, CSS, JS)
            *   4.3. Desenvolvimento Back-end (PHP, Banco de Dados)
            *   4.4. Integração com Firmware
        *   **5. Testes e Documentação**
            *   5.1. Testes Unitários e de Integração
            *   5.2. Testes de Sistema e Aceitação
            *   5.3. Documentação Técnica e de Usuário

*   **Gerenciamento de Riscos (Gerência de Projetos):** Identificar riscos potenciais e planejar respostas.
    *   **Exemplos de Riscos:** Falha de hardware, atraso na entrega de componentes, problemas de compatibilidade, falhas de segurança, dificuldade na integração. Para cada risco, definir a probabilidade, o impacto e um plano de mitigação ou contingência.

#### Quinta-feira: Validação com eletrônica e automação (esquema elétrico, escolha de sensores/atuadores).

Nesta fase do Projeto Integrador, o foco é na validação dos aspectos de **eletrônica e automação**, garantindo que o projeto seja fisicamente viável e que os componentes escolhidos atendam aos requisitos.

*   **Esquema Elétrico:** Desenvolver o diagrama esquemático do circuito eletrônico. Isso inclui:
    *   **Microcontrolador:** Arduino, Raspberry Pi ou outro.
    *   **Sensores:** Conexão dos sensores (temperatura, luz, presença) ao microcontrolador, incluindo resistores de pull-up/pull-down, se necessário.
    *   **Atuadores:** Conexão dos atuadores (LEDs, relés) ao microcontrolador, utilizando drivers de potência (transistores, ULN2003) se a corrente exigida for maior do que a que o microcontrolador pode fornecer diretamente.
    *   **Fonte de Alimentação:** Detalhar a fonte de alimentação para o microcontrolador e para os atuadores, garantindo que a corrente e a tensão sejam adequadas.
    *   **Conectividade:** Indicar as conexões de rede (Ethernet, Wi-Fi) e outras interfaces (USB, serial).
    *   **Software de Desenho de Esquemas:** Utilizar ferramentas como Fritzing, Eagle, KiCad ou Altium Designer para criar o esquema elétrico profissionalmente.

*   **Escolha de Sensores e Atuadores:** Com base nos requisitos funcionais e não funcionais, selecionar os componentes eletrônicos mais adequados:
    *   **Sensores:** Considerar precisão, alcance, tipo de saída (analógica/digital), custo, facilidade de integração e consumo de energia. Ex: DHT11/DHT22 para temperatura/umidade, LDR para luz, PIR para presença.
    *   **Atuadores:** Considerar a potência necessária, tipo de controle (digital, PWM), custo e facilidade de integração. Ex: LEDs para indicação, relés para acionar cargas AC, motores de passo para controle de posição.

*   **Validação da Lógica de Automação:**
    *   Revisar a lógica de controle do firmware para garantir que ela atenda aos requisitos (ex: ligar a luz se a luminosidade estiver baixa e houver presença).
    *   Considerar cenários de falha e como o sistema deve reagir (ex: o que acontece se um sensor falhar?).
    *   Esboçar o fluxo de dados desde o sensor, passando pelo microcontrolador, até o dashboard web e vice-versa.

#### Sexta-feira: Apresentação dos planos (envio de esboço para feedback do chatbot – simulado).

O último dia do Módulo II é dedicado à **apresentação dos planos** do Projeto Integrador. Em um cenário real de chatbot, isso simularia o envio de um esboço ou resumo do projeto para feedback, consolidando o aprendizado e preparando para a fase de implementação.

*   **Conteúdo da Apresentação (Esboço):** O aluno deve ser capaz de apresentar um resumo conciso e claro do projeto, incluindo:
    *   **Título do Projeto:** (Ex: Sistema de Automação Residencial Inteligente)
    *   **Objetivos:** O que o projeto pretende alcançar (Ex: Monitorar e controlar iluminação e temperatura de uma residência via interface web).
    *   **Requisitos Principais:** Listar os requisitos funcionais e não funcionais mais importantes.
    *   **Arquitetura Proposta:** Um diagrama simples mostrando os componentes de hardware (sensores, atuadores, microcontrolador) e software (firmware, backend, frontend) e como eles se comunicam.
    *   **Tecnologias a Serem Utilizadas:** Listar as principais tecnologias (Ex: Arduino, Python/PHP para backend, HTML/CSS/JS para frontend, MySQL para banco de dados).
    *   **EAP Simplificada:** Apresentar os principais pacotes de trabalho e entregas.
    *   **Principais Riscos Identificados:** E as estratégias de mitigação.
    *   **Cronograma Estimado:** Uma estimativa de tempo para as principais fases.

*   **Feedback do Chatbot (Simulado):** O chatbot pode simular um feedback construtivo, fazendo perguntas como:
    *   "Como você planeja lidar com a segurança dos dados dos usuários no dashboard web?"
    *   "Você considerou a escalabilidade do sistema para adicionar mais dispositivos no futuro?"
    *   "Qual será a interface de usuário para o controle dos dispositivos?"
    *   "Como você vai testar a integração entre o hardware e o software?"

*   **Importância do Feedback:** Esta etapa reforça a importância da comunicação e da iteração no desenvolvimento de projetos, permitindo ajustes e melhorias antes da execução detalhada.

---
## Módulo III – DESENVOLVIMENTO WEB, BANCO DE DADOS E PROJETO

### Semana 15 – Design UX com Figma (básico → avançado)

#### Segunda-feira: UX vs UI: fundamentos de experiência do usuário (pesquisa, personas, jornada do usuário). Wireframes de baixa fidelidade.

No mundo do desenvolvimento de produtos digitais, **UX (User Experience - Experiência do Usuário)** e **UI (User Interface - Interface do Usuário)** são termos frequentemente usados, mas com significados distintos e complementares. Compreender a diferença é o primeiro passo para criar produtos digitais eficazes e agradáveis.

*   **UX (User Experience):** Refere-se a toda a experiência que um usuário tem ao interagir com um produto, serviço ou sistema. Não se trata apenas da aparência, mas de como o usuário se sente, quão fácil é usar, quão eficiente é e se atende às suas necessidades. O UX design foca em tornar o produto útil, usável e desejável. Abrange aspectos como:
    *   **Pesquisa de Usuário:** Coleta de informações sobre os usuários, suas necessidades, comportamentos e motivações através de entrevistas, pesquisas, testes de usabilidade e análise de dados.
    *   **Personas:** Representações fictícias e arquetípicas dos usuários-alvo, criadas com base em dados de pesquisa. Elas ajudam a equipe a entender quem são os usuários, seus objetivos, dores e comportamentos.
    *   **Jornada do Usuário:** Um mapa visual que ilustra o caminho que um usuário percorre para atingir um objetivo específico ao interagir com um produto ou serviço. Ajuda a identificar pontos de dor e oportunidades de melhoria na experiência.

*   **UI (User Interface):** Refere-se à interface visual e interativa de um produto digital. É o que o usuário vê e com o que interage: botões, ícones, tipografia, cores, layouts, campos de entrada. O UI design foca na estética, na consistência visual e na interatividade da interface, garantindo que ela seja atraente e fácil de usar.

*   **Wireframes de Baixa Fidelidade:** São representações esquemáticas e simplificadas da estrutura e do layout de uma interface de usuário. Eles são criados nas fases iniciais do design para focar na funcionalidade, no fluxo de informações e na hierarquia do conteúdo, sem se preocupar com detalhes visuais. Podem ser feitos à mão ou com ferramentas digitais simples.

#### Terça-feira: Introdução ao Figma: interface, frames, shapes, texto, imagens. Componentes e variações.

**Figma** é uma ferramenta de design de interface de usuário e prototipagem baseada em navegador, amplamente utilizada por designers UX/UI. Sua natureza colaborativa e baseada em nuvem o torna ideal para equipes. Esta aula introduz os elementos fundamentais da ferramenta.

*   **Interface do Figma:** A interface do Figma é intuitiva e organizada, geralmente dividida em:
    *   **Barra de Ferramentas:** No topo, contém ferramentas para seleção, criação de formas, texto, caneta, etc.
    *   **Painel de Camadas (Layers Panel):** À esquerda, mostra a hierarquia de todos os elementos na tela.
    *   **Painel de Propriedades (Properties Panel):** À direita, permite ajustar as propriedades de elementos selecionados (cor, tamanho, tipografia, efeitos).
    *   **Canvas:** A área central onde o design é criado.

*   **Frames:** São as telas ou artboards onde o design é construído. No Figma, frames são contêineres que podem representar telas de aplicativos, páginas web, ou qualquer outra área de design. Eles são fundamentais para organizar o trabalho e definir os limites do design.

*   **Shapes (Formas):** O Figma oferece ferramentas para criar formas básicas como retângulos, círculos, linhas, polígonos e estrelas. Essas formas são os blocos construtivos de qualquer interface.

*   **Texto:** A ferramenta de texto permite adicionar e formatar texto, essencial para rótulos, títulos, parágrafos e qualquer conteúdo textual na interface. Propriedades como fonte, tamanho, cor, alinhamento e espaçamento podem ser ajustadas.

*   **Imagens:** Imagens podem ser importadas e inseridas nos designs. O Figma permite redimensionar, cortar e aplicar máscaras a imagens, integrando-as perfeitamente ao layout.

*   **Componentes e Variações:**
    *   **Componentes:** São elementos de interface reutilizáveis (ex: botões, campos de entrada, ícones). Ao criar um componente mestre, todas as suas instâncias (cópias) herdam suas propriedades. Alterar o componente mestre atualiza automaticamente todas as suas instâncias, garantindo consistência e eficiência no design.
    *   **Variações (Variants):** Permitem agrupar componentes relacionados que têm diferentes estados ou opções (ex: um botão pode ter estados "padrão", "hover", "clicado" ou tamanhos "pequeno", "médio", "grande"). As variações simplificam a organização e o uso de componentes, tornando o design system mais robusto.

#### Quarta-feira: Prototipagem interativa: links entre telas, animações, smart animate. Teste de usabilidade com protótipo.

A **prototipagem interativa** é uma etapa crucial no processo de design, permitindo simular a experiência do usuário com o produto antes mesmo de ele ser desenvolvido. O Figma oferece poderosas ferramentas para criar protótipos realistas.

*   **Links entre Telas (Flows):** No modo de protótipo do Figma, é possível criar interações clicáveis entre diferentes frames (telas). Isso simula a navegação do usuário pelo aplicativo ou site, permitindo que ele clique em botões, links e outros elementos para ir de uma tela para outra. É a base para testar o fluxo do usuário.

*   **Animações:** O Figma permite adicionar animações simples às interações, como transições de tela (deslizar, empurrar, dissolver) e efeitos em elementos individuais (aparecer, desaparecer, mover). Isso torna o protótipo mais dinâmico e realista, proporcionando uma experiência mais próxima do produto final.

*   **Smart Animate:** Uma funcionalidade avançada do Figma que cria transições e animações complexas de forma inteligente. Se dois frames contêm camadas com o mesmo nome, o Smart Animate interpola automaticamente as propriedades (posição, tamanho, cor, rotação) entre elas, criando animações suaves e sofisticadas com pouco esforço do designer.

*   **Teste de Usabilidade com Protótipo:** Uma vez que o protótipo interativo é criado, ele pode ser usado para realizar testes de usabilidade. Nesses testes, usuários reais interagem com o protótipo enquanto suas ações e feedback são observados. O objetivo é identificar problemas de usabilidade, pontos de dor e áreas de melhoria na interface e no fluxo do usuário. O Figma facilita o compartilhamento de protótipos para testes remotos ou presenciais, e a coleta de feedback.

#### Quinta-feira: Autolayout, constraints, grids responsivos. Design system (cores, tipografia, espaçamentos).

Para criar designs eficientes, responsivos e escaláveis, o Figma oferece recursos avançados de layout e organização, além da capacidade de construir um **Design System** robusto.

*   **Autolayout:** Uma funcionalidade poderosa do Figma que permite criar layouts dinâmicos e responsivos. Com o Autolayout, os elementos dentro de um frame ou grupo se ajustam automaticamente quando o conteúdo é adicionado, removido ou redimensionado. Isso é extremamente útil para criar componentes como botões (que se expandem com o texto), listas ou cards, garantindo que o espaçamento e o alinhamento sejam mantidos de forma consistente.

*   **Constraints (Restrições):** Permitem definir como os elementos se comportam quando o frame pai é redimensionado. Por exemplo, um elemento pode ser fixado ao topo e à esquerda, esticar horizontalmente, ou permanecer centralizado. As constraints são essenciais para criar designs responsivos que se adaptam a diferentes tamanhos de tela.

*   **Grids Responsivos:** O Figma suporta a criação de sistemas de grid (colunas, linhas, layout) que ajudam a alinhar elementos e criar layouts consistentes. Ao combinar grids com constraints e autolayout, é possível projetar interfaces que se adaptam perfeitamente a diferentes dispositivos e orientações (desktop, tablet, mobile).

*   **Design System:** É um conjunto completo de padrões, diretrizes e componentes reutilizáveis que garantem a consistência e a eficiência no design e desenvolvimento de produtos digitais. Um Design System bem construído inclui:
    *   **Cores:** Uma paleta de cores definida, com cores primárias, secundárias, de texto, de fundo, de erro, etc., e suas respectivas variáveis ou tokens.
    *   **Tipografia:** Uma hierarquia de fontes, tamanhos, pesos e espaçamentos de linha para títulos, subtítulos, corpo de texto, etc.
    *   **Espaçamentos:** Um sistema de espaçamento consistente (baseado em múltiplos de 4, 8 ou 10 pixels) para margens, preenchimentos e lacunas entre elementos.
    *   **Componentes:** Uma biblioteca de componentes reutilizáveis (botões, campos de entrada, cards, modais) com suas variações e estados.
    *   **Ícones:** Uma biblioteca de ícones padronizados.
    *   **Diretrizes:** Regras sobre como e quando usar cada elemento do Design System.

#### Sexta-feira: Plugins avançados, versionamento com Figma Branch, colaboração em tempo real. Exportação de assets e entrega para devs.

Esta aula explora recursos avançados do Figma que otimizam o fluxo de trabalho de design, a colaboração em equipe e a entrega para o desenvolvimento.

*   **Plugins Avançados:** O Figma possui uma vasta biblioteca de plugins desenvolvidos pela comunidade e por terceiros, que estendem suas funcionalidades. Esses plugins podem automatizar tarefas repetitivas, gerar dados fictícios, integrar com outras ferramentas, verificar acessibilidade, organizar camadas e muito mais. Exemplos: Unsplash (para imagens), Content Reel (para dados), Stark (para acessibilidade).

*   **Versionamento com Figma Branch (Ramificação):** Para equipes maiores e projetos complexos, o Figma oferece funcionalidades de versionamento semelhantes às de sistemas de controle de versão de código (como Git). O Figma Branch permite que designers trabalhem em suas próprias "ramificações" de um arquivo principal, fazendo alterações sem afetar o trabalho de outros. Uma vez que o trabalho está pronto, a ramificação pode ser revisada e mesclada de volta ao arquivo principal, garantindo um fluxo de trabalho organizado e evitando conflitos.

*   **Colaboração em Tempo Real:** Uma das maiores vantagens do Figma é sua capacidade de colaboração em tempo real. Múltiplos designers podem trabalhar no mesmo arquivo simultaneamente, vendo as alterações uns dos outros em tempo real. Isso facilita a comunicação, a revisão e a tomada de decisões em equipe, tornando o processo de design mais ágil e eficiente.

*   **Exportação de Assets e Entrega para Desenvolvedores:** O Figma simplifica o processo de entrega do design para a equipe de desenvolvimento:
    *   **Exportação de Assets:** Designers podem exportar facilmente ícones, imagens e outros elementos gráficos em diferentes formatos (PNG, JPG, SVG, PDF) e tamanhos, otimizados para web ou mobile.
    *   **Modo Desenvolvedor (Dev Mode):** O Figma possui um modo específico para desenvolvedores que permite inspecionar elementos do design, copiar códigos CSS, Swift, Kotlin ou React Native, obter medidas, espaçamentos e especificações de cores. Isso agiliza a implementação, reduzindo a necessidade de comunicação constante entre designers e desenvolvedores.
    *   **Links de Compartilhamento:** Designers podem compartilhar links para o arquivo do Figma, permitindo que desenvolvedores e outros stakeholders visualizem o design, protótipos e deixem comentários diretamente na ferramenta.

---
### Semana 16 – Programação Web (front-end)

#### Segunda-feira: HTML5: estrutura básica, tags semânticas (header, section, article), formulários, inputs, validação HTML.

O **desenvolvimento web front-end** é a parte de um site ou aplicação web com a qual o usuário interage diretamente. Ele é responsável pela apresentação visual e pela interatividade. A base de qualquer página web é o **HTML (HyperText Markup Language)**, que define a estrutura e o conteúdo.

*   **HTML5:** É a versão mais recente do HTML, que introduziu novos recursos para melhorar a semântica, a multimídia e a interatividade das páginas web.

*   **Estrutura Básica de um Documento HTML:**
    ```html
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Título da Página</title>
    </head>
    <body>
        <!-- Conteúdo da página aqui -->
    </body>
    </html>
    ```
    *   `<!DOCTYPE html>`: Declara o tipo de documento como HTML5.
    *   `<html lang="pt-br">`: Elemento raiz que define o idioma da página.
    *   `<head>`: Contém metadados sobre a página (título, codificação de caracteres, links para CSS e JS).
    *   `<body>`: Contém todo o conteúdo visível da página.

*   **Tags Semânticas:** HTML5 introduziu tags que descrevem o significado do conteúdo, melhorando a acessibilidade e o SEO (Search Engine Optimization). Exemplos:
    *   `<header>`: Representa o cabeçalho de uma seção ou da página, geralmente contendo logotipos, títulos e navegação.
    *   `<nav>`: Contém links de navegação.
    *   `<main>`: Representa o conteúdo principal do `<body>`.
    *   `<section>`: Agrupa conteúdo tematicamente relacionado.
    *   `<article>`: Representa um conteúdo independente e auto-contido (ex: post de blog, notícia).
    *   `<aside>`: Conteúdo relacionado, mas separado do conteúdo principal (ex: barra lateral).
    *   `<footer>`: Representa o rodapé de uma seção ou da página.

*   **Formulários (`<form>`):** Usados para coletar dados do usuário. O elemento `<form>` define um formulário HTML, e seus atributos `action` (para onde os dados serão enviados) e `method` (GET ou POST) são importantes.

*   **Inputs (`<input>`):** Elementos interativos dentro de um formulário para coletar diferentes tipos de dados. O atributo `type` define o tipo de entrada:
    *   `text`: Campo de texto simples.
    *   `password`: Campo para senhas (caracteres ocultos).
    *   `email`: Campo para endereços de e-mail (com validação básica).
    *   `number`: Campo para números.
    *   `date`: Campo para datas.
    *   `checkbox`: Caixa de seleção.
    *   `radio`: Botão de opção (seleção única).
    *   `submit`: Botão para enviar o formulário.
    *   `file`: Para upload de arquivos.

*   **Validação HTML5:** O HTML5 introduziu atributos para validação de formulários diretamente no navegador, sem a necessidade de JavaScript:
    *   `required`: O campo não pode ser deixado em branco.
    *   `minlength`/`maxlength`: Define o número mínimo/máximo de caracteres.
    *   `min`/`max`: Define o valor mínimo/máximo para campos numéricos.
    *   `pattern`: Define uma expressão regular que o valor do campo deve corresponder.
    *   `type="email"`, `type="url"`: Fornecem validação de formato básica.

#### Terça-feira: CSS3: seletores, box model, flexbox, grid. Responsividade (media queries) e variáveis CSS.

**CSS (Cascading Style Sheets)** é a linguagem usada para estilizar documentos HTML, controlando a apresentação visual das páginas web. O **CSS3** trouxe muitas funcionalidades avançadas para design e layout.

*   **Seletores CSS:** Usados para "selecionar" os elementos HTML que você deseja estilizar. Exemplos:
    *   **Seletor de Tipo:** `p { color: blue; }` (seleciona todos os parágrafos).
    *   **Seletor de Classe:** `.minha-classe { font-size: 16px; }` (seleciona elementos com `class="minha-classe"`).
    *   **Seletor de ID:** `#meu-id { background-color: #eee; }` (seleciona o elemento com `id="meu-id"`).
    *   **Seletores de Atributo:** `input[type="text"] { border: 1px solid gray; }`.
    *   **Seletores Combinadores:** `div p` (parágrafos dentro de divs), `div > p` (parágrafos filhos diretos de divs).
    *   **Pseudo-classes:** `:hover`, `:focus`, `:nth-child()`, etc.

*   **Box Model (Modelo de Caixa):** Todo elemento HTML é tratado como uma caixa retangular. O box model descreve como o espaço é ocupado por um elemento, incluindo:
    *   **Conteúdo (Content):** Onde o texto e as imagens aparecem.
    *   **Preenchimento (Padding):** Espaço entre o conteúdo e a borda.
    *   **Borda (Border):** Linha que envolve o padding e o conteúdo.
    *   **Margem (Margin):** Espaço fora da borda, separando o elemento de outros elementos.

*   **Flexbox (Flexible Box Layout):** Um módulo de layout unidimensional do CSS3 que permite organizar itens em linhas ou colunas de forma eficiente. É ideal para distribuir espaço entre itens em um contêiner e alinhar itens. É muito usado para criar barras de navegação, cards e layouts flexíveis.

*   **Grid (CSS Grid Layout):** Um módulo de layout bidimensional do CSS3 que permite organizar itens em linhas e colunas simultaneamente. É ideal para criar layouts de página complexos e responsivos, dividindo a página em áreas e posicionando elementos nessas áreas.

*   **Responsividade (Media Queries):** Permite que o design de um site se adapte a diferentes tamanhos de tela e dispositivos (desktops, tablets, smartphones). As `media queries` aplicam estilos CSS específicos com base nas características do dispositivo, como largura da tela, altura, orientação, etc.
    ```css
    /* Estilos padrão para telas maiores */
    .container { width: 960px; }

    @media (max-width: 768px) {
        /* Estilos para telas menores que 768px */
        .container { width: 100%; padding: 15px; }
    }
    ```

*   **Variáveis CSS (Custom Properties):** Permitem definir valores reutilizáveis (como cores, tamanhos de fonte, espaçamentos) que podem ser usados em todo o CSS. Isso facilita a manutenção e a consistência do design. Declaradas com `--` e acessadas com `var()`. Ex:
    ```css
    :root {
        --cor-primaria: #007bff;
        --espacamento-padrao: 16px;
    }
    button {
        background-color: var(--cor-primaria);
        padding: var(--espacamento-padrao);
    }
    ```

#### Quarta-feira: JavaScript ES6+: variáveis (let, const), funções arrow, arrays, objetos, template strings. Eventos DOM.

**JavaScript** é a linguagem de programação que torna as páginas web interativas e dinâmicas. O **ES6 (ECMAScript 2015)** e versões posteriores trouxeram muitas melhorias e novas funcionalidades que modernizaram a forma como escrevemos JavaScript.

*   **Variáveis (`let`, `const`):** Antes do ES6, `var` era a única forma de declarar variáveis. ES6 introduziu:
    *   `let`: Declara uma variável com escopo de bloco. Pode ser reatribuída, mas não redeclarada no mesmo escopo.
    *   `const`: Declara uma constante com escopo de bloco. Deve ser inicializada no momento da declaração e não pode ser reatribuída. Ideal para valores que não devem mudar.

*   **Funções Arrow (`=>`):** Uma sintaxe mais concisa para escrever funções, especialmente útil para funções anônimas. Elas também têm um comportamento diferente em relação ao `this`.
    ```javascript
    // Função tradicional
    function soma(a, b) {
        return a + b;
    }

    // Função arrow
    const somaArrow = (a, b) => a + b;
    ```

*   **Arrays:** Estruturas de dados para armazenar coleções ordenadas de itens. ES6+ trouxe novos métodos e sintaxes:
    *   `map()`, `filter()`, `reduce()`: Métodos para transformar, filtrar e reduzir arrays.
    *   `forEach()`: Para iterar sobre elementos.
    *   `spread operator (...)`: Para copiar arrays ou combiná-los.

*   **Objetos:** Estruturas de dados para armazenar coleções de pares chave-valor. ES6+ trouxe melhorias:
    *   **Shorthand Property Names:** `const nome = 'João'; const pessoa = { nome };`
    *   **Destructuring Assignment:** `const { nome, idade } = pessoa;`
    *   **Spread Operator:** Para copiar ou combinar objetos.

*   **Template Strings (Template Literals):** Permitem incorporar expressões e quebras de linha em strings de forma mais fácil, usando crases (`` ` ``) e `${}` para interpolação.
    ```javascript
    const nome = 'Mundo';
    const saudacao = `Olá, ${nome}!
Bem-vindo.`;
    ```

*   **Eventos DOM (Document Object Model):** O DOM é uma interface de programação para documentos HTML e XML. Ele representa a estrutura de uma página como uma árvore de objetos, permitindo que o JavaScript acesse e manipule o conteúdo, a estrutura e o estilo da página. Os eventos DOM são ações que ocorrem na página (ex: clique de botão, envio de formulário, carregamento da página) e que o JavaScript pode "ouvir" e responder.
    ```javascript
    const botao = document.getElementById('meuBotao');
    botao.addEventListener('click', () => {
        alert('Botão clicado!');
    });
    ```

#### Quinta-feira: JS avançado: promises, async/await, fetch API, manipulação de JSON. LocalStorage.

Esta aula aprofunda em conceitos de JavaScript que são essenciais para o desenvolvimento de aplicações web modernas, especialmente aquelas que interagem com APIs e armazenam dados localmente.

*   **Promises:** São objetos que representam a eventual conclusão (ou falha) de uma operação assíncrona e seu valor resultante. Elas fornecem uma maneira mais limpa e organizada de lidar com código assíncrono, evitando o "callback hell".
    *   `new Promise((resolve, reject) => { ... })`: Cria uma nova Promise.
    *   `.then()`: Usado para lidar com o sucesso da Promise.
    *   `.catch()`: Usado para lidar com erros da Promise.
    *   `.finally()`: Executado independentemente do sucesso ou falha.

*   **Async/Await:** Uma sintaxe moderna para trabalhar com Promises de forma mais síncrona e legível. `async` define uma função assíncrona que pode conter uma expressão `await`. `await` pausa a execução da função `async` até que a Promise seja resolvida.
    ```javascript
    async function buscarDados() {
        try {
            const resposta = await fetch('https://api.example.com/data');
            const dados = await resposta.json();
            console.log(dados);
        } catch (erro) {
            console.error('Erro ao buscar dados:', erro);
        }
    }
    buscarDados();
    ```

*   **Fetch API:** Uma interface moderna e baseada em Promises para fazer requisições de rede (HTTP) para buscar recursos (como APIs). Substitui o antigo `XMLHttpRequest`.
    *   `fetch(url, options)`: Retorna uma Promise que resolve para o objeto `Response`.
    *   `response.json()`: Método do objeto `Response` que retorna uma Promise que resolve para o corpo da resposta como um objeto JSON.

*   **Manipulação de JSON (JavaScript Object Notation):** JSON é um formato leve de troca de dados, amplamente utilizado em APIs web. JavaScript tem métodos nativos para trabalhar com JSON:
    *   `JSON.parse(string)`: Converte uma string JSON em um objeto JavaScript.
    *   `JSON.stringify(object)`: Converte um objeto JavaScript em uma string JSON.

*   **LocalStorage:** Uma API de armazenamento web que permite que aplicações web armazenem dados localmente no navegador do usuário, sem data de expiração. Os dados armazenados no LocalStorage persistem mesmo após o navegador ser fechado e reaberto. É ideal para armazenar pequenas quantidades de dados que não precisam ser enviados para o servidor a cada requisição.
    *   `localStorage.setItem(key, value)`: Armazena um par chave-valor.
    *   `localStorage.getItem(key)`: Recupera um valor pela chave.
    *   `localStorage.removeItem(key)`: Remove um item pela chave.
    *   `localStorage.clear()`: Limpa todo o LocalStorage.

#### Sexta-feira: Framework front-end (introdução React ou Vue): componentes, props, estado, ciclo de vida. Integração com APIs.

Para construir interfaces de usuário complexas e reativas, os desenvolvedores front-end frequentemente utilizam **frameworks ou bibliotecas JavaScript**. Esta aula introduz os conceitos fundamentais de frameworks como React ou Vue.

*   **Frameworks/Bibliotecas Front-end (React ou Vue):** São ferramentas que fornecem uma estrutura e um conjunto de funcionalidades para facilitar o desenvolvimento de interfaces de usuário interativas e escaláveis. Eles promovem a modularidade e a reatividade.
    *   **React:** Uma biblioteca JavaScript para construir interfaces de usuário, mantida pelo Facebook. Baseia-se em componentes e um DOM virtual para otimizar a renderização.
    *   **Vue.js:** Um framework JavaScript progressivo para construir interfaces de usuário. É conhecido por sua facilidade de aprendizado e flexibilidade.

*   **Componentes:** São os blocos construtivos fundamentais de uma aplicação construída com React ou Vue. Cada componente é uma peça de UI independente e reutilizável que encapsula sua própria lógica e aparência. Ex: um botão, um cabeçalho, um card de produto.

*   **Props (Properties):** São uma forma de passar dados de um componente pai para um componente filho. As props são somente leitura, o que significa que um componente filho não deve modificar as props que recebeu de seu pai. Isso garante um fluxo de dados unidirecional e previsível.

*   **Estado (State):** É um objeto JavaScript que contém dados que podem mudar ao longo do tempo e que afetam a renderização de um componente. Quando o estado de um componente muda, o componente é re-renderizado para refletir essa mudança. O estado é gerenciado internamente pelo componente.

*   **Ciclo de Vida de um Componente:** Refere-se aos diferentes estágios pelos quais um componente passa desde sua criação até sua destruição. Cada framework tem seus próprios métodos de ciclo de vida que podem ser usados para executar código em momentos específicos (ex: quando o componente é montado, atualizado ou desmontado).

*   **Integração com APIs:** Frameworks front-end são frequentemente usados para consumir dados de APIs (Application Programming Interfaces) back-end. Isso envolve:
    *   Fazer requisições HTTP (usando `fetch` ou bibliotecas como `axios`) para endpoints da API.
    *   Processar as respostas (geralmente em JSON).
    *   Atualizar o estado do componente com os dados recebidos.
    *   Renderizar a interface do usuário com os novos dados.

---
### Semana 17 – Conhecendo PHP e suas Funções

#### Segunda-feira: Introdução ao PHP: instalação (XAMPP/WAMP), sintaxe básica, variáveis superglobais ($_GET, $_POST, $_SESSION).

**PHP (Hypertext Preprocessor)** é uma linguagem de script de código aberto, amplamente utilizada para desenvolvimento web back-end. Ela é executada no servidor e gera conteúdo HTML que é enviado para o navegador do cliente. É conhecida por sua facilidade de aprendizado e vasta comunidade.

*   **Instalação (XAMPP/WAMP):** Para desenvolver em PHP localmente, é necessário um ambiente de servidor web. Ferramentas como XAMPP (para Windows, Apache, MySQL, PHP, Perl) ou WAMP (Windows, Apache, MySQL, PHP) fornecem um pacote completo e fácil de instalar, incluindo o servidor Apache, o banco de dados MySQL e o interpretador PHP.

*   **Sintaxe Básica do PHP:**
    *   Os scripts PHP são incorporados em documentos HTML e são delimitados por `<?php` e `?>`.
    *   Cada instrução PHP termina com um ponto e vírgula (`;`).
    *   Comentários podem ser de linha única (`//` ou `#`) ou de múltiplas linhas (`/* ... */`).
    *   Variáveis são declaradas com o sinal de dólar (`$`) seguido do nome da variável (ex: `$nome = "João";`).
    *   A função `echo` ou `print` é usada para exibir saída no navegador.

*   **Variáveis Superglobais:** São arrays associativos pré-definidos no PHP que contêm informações sobre o ambiente, o servidor, o usuário e os dados enviados. As mais comuns são:
    *   `$_GET`: Contém os dados enviados via método HTTP GET (visíveis na URL). Usado para passar dados pequenos e não sensíveis.
    *   `$_POST`: Contém os dados enviados via método HTTP POST (não visíveis na URL). Usado para enviar dados maiores e mais sensíveis, como formulários.
    *   `$_REQUEST`: Contém os dados de `$_GET`, `$_POST` e `$_COOKIE`.
    *   `$_SESSION`: Usado para armazenar informações do usuário entre diferentes páginas de um site, mantendo o estado da sessão.
    *   `$_SERVER`: Contém informações sobre o servidor e o ambiente de execução.

#### Terça-feira: Estruturas de controle (if, switch, for, while). Funções internas (string, array, matemática). Funções definidas pelo usuário.

As **estruturas de controle** são fundamentais em qualquer linguagem de programação, permitindo que o código tome decisões e execute blocos de instruções repetidamente. O PHP oferece as estruturas clássicas:

*   **Estruturas Condicionais:**
    *   `if`, `else if`, `else`: Executa um bloco de código se uma condição for verdadeira. Permite múltiplos caminhos.
    *   `switch`: Avalia uma expressão e executa diferentes blocos de código com base em diferentes valores possíveis da expressão.

*   **Estruturas de Repetição (Loops):**
    *   `for`: Repete um bloco de código um número específico de vezes. Ideal quando o número de iterações é conhecido.
    *   `while`: Repete um bloco de código enquanto uma condição for verdadeira. A condição é verificada antes de cada iteração.
    *   `do...while`: Semelhante ao `while`, mas garante que o bloco de código seja executado pelo menos uma vez, pois a condição é verificada após a primeira iteração.
    *   `foreach`: Usado para iterar sobre elementos de arrays ou objetos, de forma mais simples e legível.

*   **Funções Internas (Built-in Functions):** O PHP possui uma vasta biblioteca de funções pré-definidas para realizar diversas tarefas:
    *   **Funções de String:** `strlen()` (tamanho da string), `str_replace()` (substituir parte da string), `substr()` (extrair substring), `trim()` (remover espaços em branco).
    *   **Funções de Array:** `count()` (número de elementos), `array_push()` (adicionar elemento), `array_pop()` (remover último elemento), `sort()` (ordenar array), `in_array()` (verificar existência de elemento).
    *   **Funções Matemáticas:** `rand()` (gerar número aleatório), `sqrt()` (raiz quadrada), `round()` (arredondar), `max()`, `min()`.

*   **Funções Definidas pelo Usuário:** Permitem agrupar um bloco de código que realiza uma tarefa específica, tornando o código mais modular, reutilizável e fácil de manter. São declaradas com a palavra-chave `function`.
    ```php
    function saudacao($nome) {
        return "Olá, " . $nome . "!";
    }
    echo saudacao("Maria"); // Saída: Olá, Maria!
    ```

#### Quarta-feira: Programação orientada a objetos em PHP: classes, propriedades, métodos, construtor, herança, interfaces.

A **Programação Orientada a Objetos (POO)** é um paradigma de programação que organiza o código em torno de "objetos", que são instâncias de "classes". A POO em PHP permite criar código mais modular, reutilizável e fácil de manter, especialmente em projetos grandes e complexos.

*   **Classes:** São "moldes" ou "plantas" para criar objetos. Elas definem as características (propriedades) e os comportamentos (métodos) que os objetos terão. Uma classe é declarada com a palavra-chave `class`.

*   **Objetos:** São instâncias de uma classe. Cada objeto tem suas próprias propriedades e pode executar os métodos definidos na classe.
    ```php
    class Carro {
        // Propriedades
        public $marca;
        public $modelo;

        // Construtor
        public function __construct($marca, $modelo) {
            $this->marca = $marca;
            $this->modelo = $modelo;
        }

        // Método
        public function exibirDetalhes() {
            return "Marca: " . $this->marca . ", Modelo: " . $this->modelo;
        }
    }

    $meuCarro = new Carro("Toyota", "Corolla"); // Cria um objeto
    echo $meuCarro->exibirDetalhes(); // Saída: Marca: Toyota, Modelo: Corolla
    ```

*   **Propriedades (Atributos):** São as variáveis que armazenam os dados de um objeto. Elas representam as características do objeto (ex: `$marca`, `$modelo` de um carro).

*   **Métodos:** São as funções que definem os comportamentos que um objeto pode realizar. Eles operam sobre as propriedades do objeto (ex: `exibirDetalhes()` de um carro).

*   **Construtor (`__construct()`):** É um método especial que é automaticamente chamado quando um novo objeto de uma classe é criado. É usado para inicializar as propriedades do objeto.

*   **Herança:** Permite que uma classe (classe filha ou subclasse) herde propriedades e métodos de outra classe (classe pai ou superclasse). Isso promove a reutilização de código e a criação de hierarquias de classes. A herança é implementada com a palavra-chave `extends`.

*   **Interfaces:** Definem um contrato que as classes devem seguir. Uma interface especifica quais métodos uma classe deve implementar, mas não fornece a implementação desses métodos. Isso garante que diferentes classes possam ter um comportamento comum, mesmo que implementem esse comportamento de maneiras diferentes. Implementada com a palavra-chave `implements`.

#### Quinta-feira: Tratamento de erros (try/catch), sessões e cookies. Envio de emails com mail() e PHPMailer.

Esta aula aborda aspectos cruciais para a robustez e funcionalidade de aplicações web em PHP: como lidar com erros, gerenciar o estado do usuário e enviar comunicações.

*   **Tratamento de Erros (`try/catch`):** Em PHP, o tratamento de exceções com `try/catch` é a forma recomendada de lidar com erros que podem interromper a execução do script. Isso permite que o programa reaja a situações inesperadas de forma controlada, em vez de falhar completamente.
    *   `try`: Bloco de código onde o erro pode ocorrer.
    *   `catch (Exception $e)`: Bloco de código que é executado se uma exceção for lançada no bloco `try`. A variável `$e` contém informações sobre a exceção.
    *   `finally`: (Opcional) Bloco de código que é sempre executado, independentemente de uma exceção ter sido lançada ou não.

*   **Sessões:** São um mecanismo para armazenar informações do usuário no servidor entre diferentes requisições HTTP. Como o HTTP é um protocolo stateless (sem estado), as sessões permitem manter o estado do usuário (ex: usuário logado, itens no carrinho de compras) enquanto ele navega pelo site.
    *   `session_start()`: Deve ser chamada no início de cada página que usa sessões.
    *   `$_SESSION`: Array superglobal usado para armazenar e acessar variáveis de sessão.
    *   `session_destroy()`: Destrói todas as variáveis de sessão e a sessão atual.

*   **Cookies:** São pequenos arquivos de texto que o servidor envia para o navegador do cliente, que os armazena e os envia de volta ao servidor em requisições subsequentes. São usados para lembrar informações sobre o usuário (ex: preferências, login automático).
    *   `setcookie()`: Função para definir um cookie (nome, valor, tempo de expiração, caminho, domínio).
    *   `$_COOKIE`: Array superglobal para acessar os cookies enviados pelo navegador.
    *   **Diferença entre Sessões e Cookies:** Sessões armazenam dados no servidor (mais seguro para dados sensíveis), enquanto cookies armazenam dados no cliente (navegador). Sessões geralmente usam um cookie de sessão para identificar o usuário.

*   **Envio de Emails:**
    *   `mail()`: É uma função interna do PHP para enviar e-mails. É simples de usar, mas tem limitações e pode ser bloqueada por servidores de e-mail como spam se não for configurada corretamente.
    *   **PHPMailer:** É uma biblioteca de código aberto popular e robusta para envio de e-mails em PHP. Oferece recursos avançados como envio via SMTP (mais confiável), autenticação, anexos, HTML e e-mails com múltiplos destinatários. É a opção recomendada para aplicações profissionais.

#### Sexta-feira: PHP avançado: PDO (conexão segura com banco), prepared statements. Introdução a frameworks (Laravel/Symfony).

Esta aula explora tópicos mais avançados em PHP, essenciais para construir aplicações web seguras, eficientes e escaláveis, incluindo a interação com bancos de dados e o uso de frameworks.

*   **PDO (PHP Data Objects):** É uma extensão do PHP que fornece uma interface leve e consistente para acessar bancos de dados. Ele oferece uma camada de abstração de dados, o que significa que você pode usar o mesmo código para se conectar a diferentes tipos de bancos de dados (MySQL, PostgreSQL, SQL Server, SQLite). A principal vantagem do PDO é a segurança, especialmente contra ataques de injeção SQL.

*   **Prepared Statements (Declarações Preparadas):** São um recurso do PDO (e de outras APIs de banco de dados) que permite executar consultas SQL de forma segura e eficiente. Em vez de concatenar variáveis diretamente na string SQL, você prepara a consulta com placeholders e depois "binda" os valores a esses placeholders. Isso previne ataques de injeção SQL, pois os dados são enviados separadamente da consulta e não são interpretados como parte do código SQL.
    ```php
    $stmt = $pdo->prepare("INSERT INTO usuarios (nome, email) VALUES (:nome, :email)");
    $stmt->bindParam(":nome", $nome);
    $stmt->bindParam(":email", $email);
    $stmt->execute();
    ```

*   **Introdução a Frameworks PHP (Laravel/Symfony):** Frameworks são estruturas que fornecem um conjunto de ferramentas, bibliotecas e padrões de design para acelerar o desenvolvimento de aplicações web. Eles promovem a organização do código, a segurança, a manutenibilidade e a escalabilidade.
    *   **Laravel:** É um dos frameworks PHP mais populares e modernos. É conhecido por sua sintaxe elegante, recursos robustos (ORM Eloquent, sistema de rotas, autenticação, filas, cache) e uma vasta comunidade. É ideal para construir aplicações web de todos os tamanhos, desde pequenos projetos até sistemas corporativos complexos.
    *   **Symfony:** Um framework PHP robusto e modular, conhecido por sua flexibilidade e componentes reutilizáveis. É a base de muitos outros projetos PHP (incluindo o Laravel) e é ideal para aplicações de grande escala e alto desempenho. Possui uma curva de aprendizado um pouco mais íngreme que o Laravel.
    *   **Vantagens dos Frameworks:** Aceleração do desenvolvimento, padronização do código, segurança aprimorada, facilidade de manutenção, escalabilidade e acesso a uma vasta gama de bibliotecas e ferramentas.

---
### Semana 18 – Banco de Dados (básico → avançado)

#### Segunda-feira: Conceitos fundamentais: BD, SGBD, modelos (hierárquico, relacional, NoSQL). MER – Diagrama Entidade-Relacionamento.

Um **banco de dados (BD)** é uma coleção organizada de informações (dados) estruturadas, geralmente armazenadas eletronicamente em um sistema de computador. Ele permite o armazenamento, a recuperação, a modificação e a exclusão eficiente de dados. Para gerenciar esses dados, utilizamos um **Sistema Gerenciador de Banco de Dados (SGBD)**.

*   **SGBD (Sistema Gerenciador de Banco de Dados):** É um software que permite aos usuários e aplicações interagir com um banco de dados. Ele fornece ferramentas para criar, manter e manipular os dados, além de garantir a segurança, a integridade e a consistência dos dados. Exemplos: MySQL, PostgreSQL, Oracle, SQL Server, MongoDB.

*   **Modelos de Banco de Dados:** Diferentes formas de organizar e estruturar os dados:
    *   **Modelo Hierárquico:** Os dados são organizados em uma estrutura de árvore, onde cada registro pai pode ter vários registros filhos, mas cada filho tem apenas um pai. Foi um dos primeiros modelos, mas é inflexível para representar relações complexas.
    *   **Modelo Relacional:** O modelo mais amplamente utilizado atualmente. Os dados são organizados em tabelas (relações), que consistem em linhas (registros) e colunas (atributos). As relações entre as tabelas são estabelecidas através de chaves primárias e estrangeiras. É baseado na teoria matemática de conjuntos.
    *   **Modelo NoSQL (Not Only SQL):** Uma categoria de SGBDs que não segue o modelo relacional tradicional. São projetados para lidar com grandes volumes de dados não estruturados ou semiestruturados, oferecendo alta escalabilidade, flexibilidade e desempenho para casos de uso específicos. Exemplos: bancos de dados de documentos (MongoDB), chave-valor (Redis), colunas largas (Cassandra), grafos (Neo4j).

*   **MER (Modelo Entidade-Relacionamento):** É uma ferramenta conceitual para modelar a estrutura de um banco de dados. Ele representa as entidades (objetos do mundo real que queremos armazenar informações, ex: Cliente, Produto) e os relacionamentos entre elas. O **Diagrama Entidade-Relacionamento (DER)** é a representação gráfica do MER, utilizando símbolos para entidades, atributos e relacionamentos, além de indicar a cardinalidade (um para um, um para muitos, muitos para muitos) dos relacionamentos.

#### Terça-feira: SQL básico: CREATE, INSERT, SELECT, UPDATE, DELETE. Filtros (WHERE, LIKE, IN), ordenação (ORDER BY).

**SQL (Structured Query Language)** é a linguagem padrão para interagir com bancos de dados relacionais. Ela permite criar e manipular a estrutura do banco de dados, bem como inserir, consultar, atualizar e excluir dados. Esta aula aborda os comandos SQL básicos.

*   **Comandos DDL (Data Definition Language - Linguagem de Definição de Dados):** Usados para definir ou modificar a estrutura do banco de dados.
    *   `CREATE TABLE`: Cria uma nova tabela no banco de dados, especificando o nome da tabela e as colunas (nome, tipo de dado, restrições).
        ```sql
        CREATE TABLE Usuarios (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE
        );
        ```
    *   `ALTER TABLE`: Modifica a estrutura de uma tabela existente (adicionar/remover colunas, alterar tipos de dados).
    *   `DROP TABLE`: Exclui uma tabela do banco de dados.

*   **Comandos DML (Data Manipulation Language - Linguagem de Manipulação de Dados):** Usados para manipular os dados dentro das tabelas.
    *   `INSERT INTO`: Insere novas linhas (registros) em uma tabela.
        ```sql
        INSERT INTO Usuarios (nome, email) VALUES (
            'João Silva', 'joao.silva@example.com'
        );
        ```
    *   `SELECT`: Recupera dados de uma ou mais tabelas. É o comando mais utilizado.
        ```sql
        SELECT nome, email FROM Usuarios;
        ```
    *   `UPDATE`: Modifica dados existentes em uma tabela.
        ```sql
        UPDATE Usuarios SET email = 'novo.email@example.com' WHERE id = 1;
        ```
    *   `DELETE FROM`: Exclui linhas (registros) de uma tabela.
        ```sql
        DELETE FROM Usuarios WHERE id = 2;
        ```

*   **Filtros e Ordenação:**
    *   `WHERE`: Cláusula usada com `SELECT`, `UPDATE` e `DELETE` para especificar condições que as linhas devem satisfazer. Permite filtrar os resultados.
        ```sql
        SELECT * FROM Produtos WHERE preco > 50;
        ```
    *   `LIKE`: Operador usado com `WHERE` para buscar padrões em strings. Usa `%` (zero ou mais caracteres) e `_` (um único caractere) como curingas.
        ```sql
        SELECT * FROM Clientes WHERE nome LIKE 'A%'; -- Nomes que começam com 'A'
        ```
    *   `IN`: Operador usado com `WHERE` para especificar múltiplos valores possíveis para uma coluna.
        ```sql
        SELECT * FROM Pedidos WHERE status IN ('pendente', 'processando');
        ```
    *   `ORDER BY`: Cláusula usada com `SELECT` para ordenar os resultados de uma consulta em ordem crescente (`ASC`) ou decrescente (`DESC`) com base em uma ou mais colunas.
        ```sql
        SELECT nome, preco FROM Produtos ORDER BY preco DESC;
        ```

#### Quarta-feira: SQL intermediário: JOINs (INNER, LEFT, RIGHT, FULL), GROUP BY, funções de agregação (COUNT, AVG, SUM, MAX, MIN). Subconsultas.

Esta aula aprofunda no SQL, explorando funcionalidades que permitem consultas mais complexas e a análise de dados em bancos de dados relacionais.

*   **JOINs:** Usados para combinar linhas de duas ou mais tabelas com base em uma coluna relacionada entre elas. São essenciais para trabalhar com bancos de dados relacionais.
    *   `INNER JOIN`: Retorna apenas as linhas que têm correspondência em ambas as tabelas.
        ```sql
        SELECT P.nome, C.nome_categoria
        FROM Produtos P
        INNER JOIN Categorias C ON P.categoria_id = C.id;
        ```
    *   `LEFT JOIN` (ou `LEFT OUTER JOIN`): Retorna todas as linhas da tabela da esquerda e as linhas correspondentes da tabela da direita. Se não houver correspondência, retorna NULL para as colunas da tabela da direita.
    *   `RIGHT JOIN` (ou `RIGHT OUTER JOIN`): Retorna todas as linhas da tabela da direita e as linhas correspondentes da tabela da esquerda. Se não houver correspondência, retorna NULL para as colunas da tabela da esquerda.
    *   `FULL JOIN` (ou `FULL OUTER JOIN`): Retorna todas as linhas quando há uma correspondência em uma das tabelas. Retorna NULL onde não há correspondência.

*   **`GROUP BY`:** Cláusula usada para agrupar linhas que têm os mesmos valores em colunas especificadas em um conjunto de linhas de resumo. É frequentemente usada com funções de agregação.
    ```sql
    SELECT categoria_id, COUNT(*) AS total_produtos
    FROM Produtos
    GROUP BY categoria_id;
    ```

*   **Funções de Agregação:** Realizam um cálculo em um conjunto de linhas e retornam um único valor. São frequentemente usadas com `GROUP BY`.
    *   `COUNT()`: Conta o número de linhas.
    *   `AVG()`: Calcula a média de um conjunto de valores.
    *   `SUM()`: Calcula a soma de um conjunto de valores.
    *   `MAX()`: Retorna o valor máximo de um conjunto de valores.
    *   `MIN()`: Retorna o valor mínimo de um conjunto de valores.

*   **Subconsultas (Subqueries):** Uma consulta SQL aninhada dentro de outra consulta SQL. A subconsulta é executada primeiro e seu resultado é usado pela consulta externa. Podem ser usadas em cláusulas `WHERE`, `FROM` ou `SELECT`.
    ```sql
    -- Selecionar produtos cujo preço é maior que a média de todos os produtos
    SELECT nome, preco
    FROM Produtos
    WHERE preco > (SELECT AVG(preco) FROM Produtos);
    ```

#### Quinta-feira: Modelagem avançada: normalização (1FN, 2FN, 3FN, FNBC), índices, chaves estrangeiras, constraints. Transações e ACID.

Para construir bancos de dados robustos, eficientes e com integridade de dados, é necessário aplicar conceitos de **modelagem avançada**.

*   **Normalização:** É um processo de organização das colunas e tabelas em um banco de dados relacional para minimizar a redundância de dados e melhorar a integridade dos dados. É feita através de Formas Normais (FNs):
    *   **1ª Forma Normal (1FN):** Cada coluna deve conter valores atômicos (indivisíveis) e não deve haver grupos repetitivos de colunas.
    *   **2ª Forma Normal (2FN):** Deve estar em 1FN e todas as colunas não-chave devem ser totalmente dependentes da chave primária (elimina dependências parciais).
    *   **3ª Forma Normal (3FN):** Deve estar em 2FN e todas as colunas não-chave devem ser independentes de outras colunas não-chave (elimina dependências transitivas).
    *   **Forma Normal de Boyce-Codd (FNBC ou BCNF):** Uma forma mais rigorosa da 3FN, onde cada determinante (atributo que determina outro atributo) deve ser uma chave candidata.

*   **Índices:** São estruturas de dados especiais que melhoram a velocidade das operações de recuperação de dados em uma tabela. Eles funcionam de forma semelhante ao índice de um livro, permitindo que o SGBD encontre rapidamente as linhas desejadas sem ter que escanear a tabela inteira. No entanto, índices adicionam sobrecarga nas operações de inserção, atualização e exclusão.

*   **Chaves Estrangeiras (Foreign Keys):** São colunas (ou um conjunto de colunas) em uma tabela que referenciam a chave primária de outra tabela. Elas estabelecem um vínculo entre as tabelas e garantem a **integridade referencial**, ou seja, que os relacionamentos entre os dados sejam válidos e consistentes.

*   **Constraints (Restrições):** São regras aplicadas às colunas de uma tabela para impor a integridade dos dados. Exemplos:
    *   `PRIMARY KEY`: Garante que a coluna contenha valores únicos e não nulos, identificando unicamente cada registro.
    *   `FOREIGN KEY`: Garante a integridade referencial com outra tabela.
    *   `UNIQUE`: Garante que todos os valores em uma coluna sejam diferentes.
    *   `NOT NULL`: Garante que uma coluna não possa ter valores nulos.
    *   `CHECK`: Garante que todos os valores em uma coluna satisfaçam uma condição específica.
    *   `DEFAULT`: Define um valor padrão para uma coluna quando nenhum valor é especificado.

*   **Transações e ACID:**
    *   **Transação:** É uma sequência de uma ou mais operações de banco de dados que são executadas como uma única unidade lógica de trabalho. Uma transação deve ser concluída com sucesso (commit) ou desfeita completamente (rollback) se ocorrer um erro.
    *   **ACID:** É um acrônimo que descreve as propriedades desejáveis de uma transação de banco de dados para garantir a integridade dos dados:
        *   **Atomicidade:** Uma transação é uma unidade indivisível; ou todas as suas operações são concluídas com sucesso, ou nenhuma delas é.
        *   **Consistência:** Uma transação leva o banco de dados de um estado válido para outro estado válido, mantendo todas as regras e restrições.
        *   **Isolamento:** A execução de uma transação não deve ser afetada por outras transações concorrentes. Cada transação parece ser executada isoladamente.
        *   **Durabilidade:** Uma vez que uma transação é confirmada (commit), suas alterações são permanentes e sobreviverão a falhas do sistema.

#### Sexta-feira: NoSQL (MongoDB): documentos, coleções, CRUD, agregação. Quando usar NoSQL vs SQL. Introdução a bancos de dados em nuvem (Firebase, DynamoDB).

Esta aula explora o mundo dos bancos de dados **NoSQL**, com foco no MongoDB, e discute quando escolher entre NoSQL e SQL, além de introduzir os bancos de dados em nuvem.

*   **NoSQL (Not Only SQL):** Bancos de dados que oferecem um mecanismo para armazenar e recuperar dados que não seguem o modelo relacional tabular tradicional. Eles são projetados para casos de uso específicos que exigem alta escalabilidade, flexibilidade de esquema e desempenho para grandes volumes de dados não estruturados ou semiestruturados.

*   **MongoDB (Exemplo de Banco de Dados de Documentos):** Um dos bancos de dados NoSQL mais populares, que armazena dados em documentos flexíveis no formato BSON (uma representação binária de JSON). Os documentos são agrupados em coleções.
    *   **Documentos:** Equivalentes a linhas em bancos de dados relacionais, mas com uma estrutura mais flexível. Cada documento pode ter um esquema diferente.
    *   **Coleções:** Equivalentes a tabelas em bancos de dados relacionais, mas contêm documentos em vez de linhas.
    *   **CRUD (Create, Read, Update, Delete):** As operações básicas para manipular dados:
        *   `db.collection.insertOne()` / `insertMany()`: Inserir documentos.
        *   `db.collection.find()`: Consultar documentos.
        *   `db.collection.updateOne()` / `updateMany()`: Atualizar documentos.
        *   `db.collection.deleteOne()` / `deleteMany()`: Excluir documentos.
    *   **Agregação:** Processamento de dados para retornar resultados computados. O MongoDB oferece um poderoso pipeline de agregação para realizar operações complexas de transformação e análise de dados.

*   **Quando usar NoSQL vs SQL:**

| Característica        | SQL (Relacional)                                  | NoSQL (Não Relacional)                               |
|-----------------------|---------------------------------------------------|------------------------------------------------------|
| **Estrutura de Dados**| Tabelas com esquema fixo (linhas e colunas)       | Documentos, chave-valor, colunas largas, grafos (esquema flexível)|
| **Escalabilidade**    | Vertical (mais recursos para um único servidor)   | Horizontal (distribuição de dados em múltiplos servidores)|
| **Integridade**       | Alta (ACID, chaves estrangeiras, normalização)    | Menor (eventual consistência, BASE)                  |
| **Complexidade**      | Mais complexo para dados não estruturados         | Ideal para dados não estruturados/semiestruturados   |
| **Uso Comum**         | Aplicações transacionais, dados estruturados      | Big Data, tempo real, IoT, conteúdo dinâmico         |
| **Exemplos**          | MySQL, PostgreSQL, Oracle, SQL Server             | MongoDB, Cassandra, Redis, Neo4j                      |

*   **Introdução a Bancos de Dados em Nuvem:** São serviços de banco de dados hospedados e gerenciados por provedores de nuvem. Eles oferecem escalabilidade, alta disponibilidade, backups automáticos e gerenciamento simplificado, permitindo que os desenvolvedores se concentrem na aplicação.
    *   **Firebase (Google):** Um conjunto de serviços de desenvolvimento de aplicativos móveis e web, incluindo um banco de dados NoSQL em tempo real (Firestore/Realtime Database). Ideal para aplicações que exigem sincronização de dados em tempo real e desenvolvimento rápido.
    *   **DynamoDB (AWS):** Um serviço de banco de dados NoSQL de chave-valor e documentos totalmente gerenciado pela Amazon. Oferece desempenho de milissegundos de um dígito em qualquer escala, com alta disponibilidade e durabilidade.
    *   Outros exemplos incluem Azure Cosmos DB, Google Cloud SQL, Amazon RDS.

---
### Semana 19 – Projeto Integrador – TI (execução prática)

#### Segunda-feira: Configuração do ambiente de desenvolvimento: Git/GitHub, Docker para banco + PHP + front.

Nesta semana, o Projeto Integrador entra na fase de **execução prática**. O primeiro passo é configurar um ambiente de desenvolvimento robusto e eficiente, utilizando ferramentas essenciais para o desenvolvimento moderno de software.

*   **Git e GitHub:**
    *   **Git:** É um sistema de controle de versão distribuído que permite rastrear alterações no código-fonte durante o desenvolvimento de software. Ele permite que múltiplos desenvolvedores trabalhem no mesmo projeto simultaneamente, gerenciem diferentes versões do código, revertam alterações e resolvam conflitos.
    *   **GitHub:** É uma plataforma de hospedagem de código-fonte baseada em Git. Além de armazenar repositórios Git, o GitHub oferece funcionalidades de colaboração, como controle de acesso, gerenciamento de issues, pull requests (para revisão de código) e integração contínua. É essencial para projetos em equipe e para construir um portfólio de código.
    *   **Comandos Básicos do Git:**
        *   `git init`: Inicializa um novo repositório Git.
        *   `git clone [URL]`: Clona um repositório existente.
        *   `git add .`: Adiciona todas as alterações ao stage.
        *   `git commit -m "Mensagem"`: Salva as alterações no histórico.
        *   `git push`: Envia as alterações para o repositório remoto (GitHub).
        *   `git pull`: Baixa as alterações do repositório remoto.
        *   `git branch`: Gerencia ramificações (branches) para desenvolvimento paralelo.

*   **Docker para Ambiente de Desenvolvimento:** O Docker é uma ferramenta poderosa para criar, implantar e executar aplicações em containers. Ele permite empacotar a aplicação e todas as suas dependências em uma unidade isolada, garantindo que ela funcione de forma consistente em qualquer ambiente (desenvolvimento, teste, produção). Para o Projeto Integrador, o Docker pode ser usado para configurar facilmente:
    *   **Banco de Dados:** Executar um container MySQL ou PostgreSQL, isolado do sistema operacional hospedeiro.
    *   **Servidor PHP:** Executar um container com PHP e um servidor web (Apache ou Nginx), configurado para a aplicação.
    *   **Servidor Front-end:** Executar um container para servir a aplicação front-end (ex: Node.js para React/Vue).
    *   **Docker Compose:** Uma ferramenta para definir e executar aplicações Docker multi-container. Com um único arquivo `docker-compose.yml`, é possível configurar todos os serviços necessários (banco de dados, backend, frontend) e iniciá-los com um único comando (`docker-compose up`).

#### Terça-feira: Implementação do back-end: API REST com PHP + MySQL (rotas, controller, modelo).

Nesta etapa, o foco é na construção do **back-end** da aplicação, que será responsável por gerenciar a lógica de negócios, interagir com o banco de dados e fornecer dados para o front-end através de uma **API REST**.

*   **API REST (Representational State Transfer):** É um estilo arquitetural para sistemas distribuídos, amplamente utilizado para construir serviços web. Uma API RESTful usa requisições HTTP (GET, POST, PUT, DELETE) para acessar e manipular recursos (dados) de forma padronizada. Os dados são geralmente trocados em formato JSON.

*   **Implementação com PHP e MySQL (usando um framework como Laravel ou Symfony para melhores práticas):**
    *   **Rotas (Routes):** Definem os endpoints da API e mapeiam as requisições HTTP para as funções apropriadas no código. Ex: uma rota `GET /api/dispositivos` para listar dispositivos, `POST /api/dispositivos` para criar um novo dispositivo.
    *   **Controller (Controlador):** Contém a lógica para processar as requisições HTTP, interagir com o modelo (para acessar o banco de dados) e retornar uma resposta (geralmente JSON). O controlador atua como um intermediário entre a requisição do cliente e o modelo de dados.
    *   **Modelo (Model):** Representa a estrutura dos dados e a lógica de negócios relacionada ao banco de dados. Em frameworks PHP, um ORM (Object-Relational Mapper) como o Eloquent (Laravel) ou Doctrine (Symfony) é frequentemente usado para interagir com o banco de dados de forma orientada a objetos, abstraindo as consultas SQL diretas.
        *   **Exemplo de Fluxo:**
            1.  Requisição HTTP (ex: GET /api/dispositivos) chega ao servidor.
            2.  A rota correspondente é acionada.
            3.  O controlador chama o modelo para buscar os dispositivos no MySQL.
            4.  O modelo interage com o banco de dados (usando PDO/Prepared Statements).
            5.  O modelo retorna os dados para o controlador.
            6.  O controlador formata os dados como JSON e envia a resposta HTTP para o cliente.

#### Quarta-feira: Implementação do front-end: consumo da API com fetch/axios, exibição de dados (HTML/CSS/JS ou React).

Com o back-end e a API REST funcionando, o próximo passo é construir o **front-end** da aplicação, que será a interface com a qual o usuário interage. O front-end consumirá os dados fornecidos pela API e os exibirá de forma amigável.

*   **Consumo da API:** O front-end fará requisições HTTP para a API REST do back-end para obter, enviar, atualizar ou excluir dados. Isso pode ser feito usando:
    *   **Fetch API:** A API nativa do navegador para fazer requisições de rede, baseada em Promises (conforme visto na Semana 16).
    *   **Axios:** Uma biblioteca JavaScript popular para fazer requisições HTTP, que oferece recursos adicionais como interceptores de requisição/resposta, tratamento de erros simplificado e cancelamento de requisições.

*   **Exibição de Dados:** Uma vez que os dados são recebidos da API (geralmente em formato JSON), o front-end os processa e os exibe na interface do usuário. Isso pode ser feito de diferentes maneiras:
    *   **HTML/CSS/JS Puro:** Manipular o DOM diretamente com JavaScript para criar e atualizar elementos HTML com os dados recebidos. É adequado para aplicações mais simples.
    *   **Frameworks/Bibliotecas Front-end (React, Vue):** Para aplicações mais complexas e interativas, frameworks como React ou Vue são ideais. Eles permitem:
        *   **Componentes:** Criar componentes reutilizáveis para exibir diferentes partes dos dados (ex: um componente `CardDispositivo` para cada dispositivo).
        *   **Estado:** Gerenciar o estado da aplicação (dados recebidos da API, estado de carregamento, erros) e re-renderizar a interface automaticamente quando o estado muda.
        *   **Renderização Declarativa:** Descrever como a interface deve parecer para um determinado estado, e o framework se encarrega de atualizar o DOM de forma eficiente.

*   **Exemplo de Interação:**
    1.  O usuário acessa o dashboard web.
    2.  O front-end faz uma requisição `GET` para `/api/dispositivos`.
    3.  A API retorna uma lista de dispositivos em JSON.
    4.  O front-end processa o JSON e atualiza a interface, exibindo os dispositivos em cards ou uma tabela.
    5.  Se o usuário clica em um botão para ligar uma lâmpada, o front-end faz uma requisição `POST` ou `PUT` para `/api/dispositivos/{id}/ligar`.
    6.  A API processa a requisição, atualiza o estado do dispositivo no banco de dados e, se houver integração, envia um comando para o hardware.

#### Quinta-feira: Integração do sistema com hardware simulado (ex: enviar comando para LED via WebSocket ou serial – opcional).

Esta é a etapa onde a ponte entre o mundo do software e o mundo físico é construída. A **integração com hardware** é o ponto alto de um projeto de automação, permitindo que a aplicação web controle dispositivos reais. Para fins de aprendizado, pode-se usar hardware simulado ou real.

*   **Objetivo da Integração:** Fazer com que o dashboard web (front-end) possa enviar comandos para os dispositivos de hardware (atuadores) e receber informações dos sensores, fechando o ciclo de automação.

*   **Opções de Comunicação Software-Hardware:**
    *   **Via Serial (USB):** Se o microcontrolador (ex: Arduino) estiver conectado diretamente ao computador que executa o back-end, a comunicação pode ser feita via porta serial. O back-end (PHP) pode abrir a porta serial e enviar/receber dados. Isso é mais comum em ambientes de prototipagem local.
    *   **Via Rede (Wi-Fi/Ethernet):** Para sistemas mais distribuídos, o microcontrolador pode estar conectado à rede local e se comunicar com o back-end via protocolos de rede. Isso é mais escalável e flexível.
        *   **HTTP:** O microcontrolador pode expor uma API HTTP simples para receber comandos (ex: `GET /led/on`, `GET /led/off`).
        *   **MQTT:** Um protocolo leve de mensagens (visto na Semana 6) ideal para IoT. O microcontrolador pode se inscrever em tópicos para receber comandos e publicar dados de sensores em outros tópicos. O back-end atua como um cliente MQTT.
        *   **WebSocket:** Permite uma comunicação bidirecional e persistente entre o navegador (front-end) e o servidor (back-end), e entre o back-end e o microcontrolador. É ideal para atualizações em tempo real, como o estado de um sensor ou o acionamento de um atuador. O back-end atuaria como um servidor WebSocket e o microcontrolador como um cliente.

*   **Hardware Simulado (Opcional):** Se não houver hardware físico disponível, pode-se simular o comportamento dos dispositivos. Por exemplo:
    *   Um script Python ou Node.js pode simular um Arduino, recebendo comandos via serial ou rede e imprimindo mensagens no console como se estivesse ligando/desligando um LED.
    *   Um simulador de circuitos eletrônicos pode ser usado para visualizar o comportamento dos componentes.

*   **Desafios:** Lidar com latência, confiabilidade da comunicação, segurança (autenticação/autorização para comandos de hardware) e tratamento de erros na integração.

#### Sexta-feira: Testes finais (unitários com PHPUnit, teste de usabilidade). Documentação do projeto (README, manual do usuário).

O último dia da fase de execução prática é dedicado a garantir a qualidade do projeto através de **testes finais** e a preparar a **documentação** necessária para que o projeto seja compreendido e utilizado.

*   **Testes Finais:**
    *   **Testes Unitários (com PHPUnit para PHP):** Testar as menores unidades de código do back-end (funções, classes, métodos) isoladamente para garantir que cada parte funcione conforme o esperado. O PHPUnit é um framework de testes unitários para PHP, que permite escrever e executar testes automatizados.
    *   **Testes de Integração:** Verificar se os diferentes módulos do back-end (rotas, controladores, modelos) se comunicam corretamente entre si e com o banco de dados. Também testar a integração entre o front-end e o back-end (se as requisições API estão funcionando e os dados são exibidos corretamente).
    *   **Testes de Sistema:** Testar o sistema completo (front-end, back-end, banco de dados e, se houver, hardware) como um todo, simulando cenários de uso real para garantir que ele atenda a todos os requisitos funcionais e não funcionais.
    *   **Testes de Usabilidade:** Realizados com usuários reais (ou simulados) para avaliar a facilidade de uso, a eficiência e a satisfação com a interface do usuário (dashboard web). Observar como os usuários interagem com o sistema, identificar pontos de dificuldade e coletar feedback para melhorias.

*   **Documentação do Projeto:** Uma documentação clara e completa é essencial para que o projeto possa ser mantido, evoluído e utilizado por outras pessoas.
    *   **README.md (no GitHub):** Um arquivo Markdown na raiz do repositório que fornece uma visão geral do projeto, como configurá-lo, como executá-lo, suas funcionalidades principais, tecnologias utilizadas e instruções para contribuir. É o primeiro contato de qualquer pessoa com o projeto.
    *   **Manual do Usuário:** Um guia detalhado sobre como usar o sistema, explicando cada funcionalidade do dashboard web, como configurar dispositivos (se aplicável) e como interpretar as informações exibidas. Deve ser escrito em linguagem clara e acessível.
    *   **Documentação Técnica (Opcional, mas Recomendado):** Detalhes sobre a arquitetura do sistema, design do banco de dados (DER), diagramas de fluxo de dados, especificações da API, decisões de design e qualquer outra informação relevante para desenvolvedores que venham a trabalhar no projeto.

---
### Semana 20 – Encerramento e Próximos Passos

#### Segunda-feira: Revisão geral dos 3 módulos (mapa mental interativo – texto enviado pelo bot).

O último módulo do cronograma culmina com uma **revisão geral abrangente dos três módulos**, consolidando todo o conhecimento adquirido ao longo das 20 semanas. O objetivo é reforçar os conceitos-chave e a interconexão entre as diferentes áreas da informática.

*   **Revisão Integrada:** O bot pode enviar um texto que simule um **mapa mental interativo**, conectando os principais tópicos de cada módulo:
    *   **Módulo I (Fundamentos e Manutenção de Hardware):** Hardware, software, arquitetura de computadores, processadores, memórias, armazenamento, redes, sistemas operacionais I, lógica matemática, tópicos especiais (IoT, Big Data, Cloud).
    *   **Módulo II (Gerência, Automação e Eletrônica):** Automação (sensores, atuadores, CLPs), eletrônica (fundamentos, componentes passivos/ativos, CIs, Arduino), engenharia de software (modelos, requisitos, design, testes), gerência de projetos (ciclo de vida, EAP, riscos, Scrum), planejamento estratégico e empreendedorismo, segurança do trabalho, sistemas operacionais II (Linux, Windows Server, virtualização, containers).
    *   **Módulo III (Desenvolvimento Web, Banco de Dados e Projeto):** Design UX com Figma, programação web front-end (HTML, CSS, JavaScript, frameworks), PHP (sintaxe, POO, PDO, frameworks), banco de dados (SQL, NoSQL, modelagem, transações), projeto integrador (configuração, backend, frontend, integração, testes, documentação).

*   **Formato do Mapa Mental (Texto):** O texto pode apresentar os tópicos de forma hierárquica, com links ou referências cruzadas para que o usuário possa revisitar conceitos específicos. Pode-se usar perguntas-chave para cada área, incentivando a reflexão e a autoavaliação.

#### Terça-feira: Simulado de questões (10 perguntas objetivas) sobre hardware, redes, SO, ES, BD, PHP.

Para avaliar o aprendizado e identificar áreas que ainda precisam de reforço, um **simulado de questões objetivas** é uma ferramenta eficaz. O bot pode apresentar 10 perguntas, abrangendo os principais temas do cronograma.

*   **Estrutura do Simulado:**
    *   **Formato:** Perguntas de múltipla escolha ou verdadeiro/falso.
    *   **Abrangência:** As questões devem cobrir uma variedade de tópicos dos três módulos, garantindo que o aluno seja testado em diferentes áreas.
    *   **Exemplos de Perguntas:**
        1.  Qual componente é considerado o "cérebro" do computador?
            a) Placa-mãe b) Memória RAM c) CPU d) HD/SSD
        2.  Qual a principal função de um firewall em uma rede?
            a) Acelerar a internet b) Bloquear acessos não autorizados c) Gerenciar senhas d) Armazenar dados
        3.  Qual o modelo de processo de software que é sequencial e linear?
            a) Scrum b) Cascata c) Espiral d) Kanban
        4.  Qual a linguagem padrão para interagir com bancos de dados relacionais?
            a) HTML b) CSS c) JavaScript d) SQL
        5.  Qual a tecnologia que permite executar múltiplos sistemas operacionais em um único hardware físico?
            a) Containers b) Virtualização c) Cloud Computing d) IoT
        6.  Em PHP, qual superglobal é usada para armazenar informações do usuário entre diferentes páginas?
            a) `$_GET` b) `$_POST` c) `$_SESSION` d) `$_SERVER`
        7.  Qual o objetivo principal da normalização de banco de dados?
            a) Aumentar a redundância b) Minimizar a redundância c) Acelerar consultas d) Proteger contra vírus
        8.  Qual a principal diferença entre UX e UI?
            a) UX é sobre estética, UI é sobre funcionalidade b) UX é sobre a experiência, UI é sobre a interface c) São sinônimos d) UX é para web, UI é para mobile
        9.  Qual a ferramenta de controle de versão distribuído mais utilizada?
            a) FTP b) SVN c) Git d) Docker
        10. Qual a função de um sensor em um sistema automatizado?
            a) Executar comandos b) Armazenar dados c) Detectar grandezas físicas d) Amplificar sinais

*   **Feedback Imediato:** O bot pode fornecer feedback imediato após cada resposta ou ao final do simulado, explicando a resposta correta e o conceito relacionado.

#### Quarta-feira: Carreiras em TI: trilhas (dev front, back, fullstack, DBA, DevOps, segurança). Certificações recomendadas (CompTIA, LPIC, AWS, Scrum).

Com uma base sólida em TI, é importante explorar as diversas **trilhas de carreira** disponíveis e as **certificações** que podem impulsionar o desenvolvimento profissional. O mercado de TI é vasto e oferece muitas oportunidades.

*   **Trilhas de Carreira em TI:**
    *   **Desenvolvedor Front-end:** Foca na interface do usuário (UI) e na experiência do usuário (UX). Trabalha com HTML, CSS, JavaScript e frameworks como React, Vue ou Angular. Responsável por tudo o que o usuário vê e interage no navegador.
    *   **Desenvolvedor Back-end:** Foca na lógica de negócios, banco de dados, servidores e APIs. Trabalha com linguagens como PHP, Python, Node.js, Java e bancos de dados SQL/NoSQL. Responsável pela parte "invisível" da aplicação.
    *   **Desenvolvedor Fullstack:** Possui habilidades tanto em front-end quanto em back-end, sendo capaz de desenvolver a aplicação de ponta a ponta.
    *   **DBA (Database Administrator - Administrador de Banco de Dados):** Responsável pela instalação, configuração, manutenção, segurança e otimização de bancos de dados. Garante a disponibilidade e a integridade dos dados.
    *   **DevOps Engineer:** Atua na integração e automação dos processos de desenvolvimento e operações, utilizando ferramentas de CI/CD, containers (Docker, Kubernetes), automação de infraestrutura e monitoramento.
    *   **Engenheiro de Segurança da Informação:** Foca na proteção de sistemas, redes e dados contra ameaças cibernéticas. Envolve análise de vulnerabilidades, implementação de políticas de segurança, resposta a incidentes e conformidade com regulamentações.
    *   **Analista de Dados/Cientista de Dados:** Trabalha com coleta, limpeza, análise e interpretação de grandes volumes de dados para extrair insights e apoiar a tomada de decisões.
    *   **Engenheiro de Redes:** Projeta, implementa e gerencia a infraestrutura de rede de uma organização.
    *   **Analista de Suporte/Help Desk:** Presta suporte técnico a usuários, resolvendo problemas de hardware e software.

*   **Certificações Recomendadas:** As certificações validam o conhecimento e a experiência em áreas específicas, sendo um diferencial no mercado de trabalho.
    *   **CompTIA (A+, Network+, Security+):** Certificações de nível de entrada e intermediário que cobrem fundamentos de hardware, redes e segurança.
    *   **LPIC (Linux Professional Institute Certification):** Certificações para profissionais Linux, em diferentes níveis de proficiência.
    *   **Certificações AWS/Azure/Google Cloud:** Para profissionais que desejam atuar com computação em nuvem, validando conhecimentos em serviços específicos de cada provedor.
    *   **Certificações Scrum (CSM, PSM):** Para profissionais que atuam em projetos ágeis, validando o conhecimento do framework Scrum.
    *   **Certificações de Segurança (CISSP, CEH):** Para profissionais de segurança da informação.

#### Quinta-feira: Dicas de portfólio, LinkedIn, GitHub. Como continuar estudando sozinho (roadmaps, cursos gratuitos e pagos).

Para ter sucesso na carreira de TI, é fundamental não apenas adquirir conhecimento, mas também saber como apresentá-lo e como continuar aprendendo de forma autônoma. Esta aula oferece dicas práticas.

*   **Dicas de Portfólio:** Um portfólio é uma coleção de seus melhores trabalhos e projetos, que demonstra suas habilidades e experiência. Para profissionais de TI:
    *   **Projetos Pessoais:** Desenvolva projetos que resolvam problemas reais ou demonstrem suas habilidades em tecnologias específicas. O Projeto Integrador é um excelente exemplo.
    *   **Projetos Open Source:** Contribua para projetos de código aberto no GitHub. Isso mostra colaboração e engajamento com a comunidade.
    *   **Documentação:** Cada projeto deve ter uma boa documentação (README.md) explicando o que ele faz, como executá-lo e as tecnologias utilizadas.
    *   **Qualidade vs Quantidade:** Priorize a qualidade e a relevância dos projetos em vez de ter muitos projetos incompletos.

*   **LinkedIn:** É a principal rede social profissional. Mantenha seu perfil atualizado:
    *   **Resumo Profissional:** Destaque suas habilidades, experiências e objetivos de carreira.
    *   **Experiência:** Detalhe suas responsabilidades e conquistas em cada cargo.
    *   **Educação e Certificações:** Inclua todos os cursos, graduações e certificações relevantes.
    *   **Habilidades:** Adicione as habilidades técnicas e interpessoais que você possui.
    *   **Conexões:** Conecte-se com colegas, recrutadores e profissionais da sua área.
    *   **Atividade:** Compartilhe artigos, participe de discussões e demonstre seu conhecimento.

*   **GitHub:** É o cartão de visitas de muitos desenvolvedores. Mantenha seus repositórios organizados:
    *   **Projetos Fixados:** Destaque seus melhores projetos no seu perfil.
    *   **Commits Regulares:** Mostre que você está ativo e contribuindo.
    *   **READMEs Detalhados:** Para cada projeto, forneça um README claro e completo.
    *   **Organização:** Use nomes de repositórios claros e organize seu código.

*   **Como Continuar Estudando Sozinho:** A TI é uma área de constante mudança, e o aprendizado contínuo é essencial.
    *   **Roadmaps de Carreira:** Utilize roadmaps online (ex: roadmap.sh) para guiar seus estudos em uma trilha específica (front-end, back-end, DevOps).
    *   **Cursos Gratuitos:** Plataformas como freeCodeCamp, The Odin Project, Coursera (cursos auditados), edX, YouTube (canais especializados).
    *   **Cursos Pagos:** Udemy, Alura, DIO, Udacity, Pluralsight, bootcamps. Invista em cursos que ofereçam conteúdo aprofundado e projetos práticos.
    *   **Documentação Oficial:** A melhor fonte de informação para qualquer tecnologia.
    *   **Comunidades Online:** Fóruns, grupos de Discord/Telegram, Stack Overflow.
    *   **Projetos Pessoais:** A melhor forma de aprender é fazendo. Aplique o que você aprende em projetos reais.

#### Sexta-feira: Mensagem de conclusão + convite para refazer o cronograma (loop) ou avançar para tópicos especializados (IA, mobile, cyber).

Este é o último dia do cronograma de 20 semanas, marcando a conclusão de uma jornada de aprendizado intensiva. A mensagem final do bot deve ser inspiradora, reforçando o valor do conhecimento adquirido e oferecendo caminhos para o futuro.

*   **Mensagem de Conclusão (Exemplo):**

    "Parabéns! Você concluiu com sucesso o nosso cronograma de 20 semanas em Tecnologia da Informação. Ao longo deste período, você explorou os fundamentos do hardware, mergulhou nas redes de computadores, compreendeu os sistemas operacionais, dominou a lógica matemática, desvendou os segredos da automação e eletrônica, aplicou os princípios da engenharia e gerência de software, e construiu uma base sólida em desenvolvimento web e banco de dados.

    Este é um marco significativo em sua jornada. Você não apenas adquiriu um vasto conhecimento técnico, mas também desenvolveu o pensamento crítico, a capacidade de resolver problemas e a autonomia para continuar aprendendo. Lembre-se: a tecnologia está em constante evolução, e a curiosidade e a dedicação ao aprendizado contínuo serão seus maiores aliados."

*   **Convite para Refazer o Cronograma (Loop):**

    "Se você sente que precisa solidificar ainda mais algum conceito ou deseja revisar todo o conteúdo para fixar o aprendizado, sinta-se à vontade para iniciar o cronograma novamente. A repetição é uma poderosa ferramenta de memorização e aprofundamento."

*   **Convite para Avançar para Tópicos Especializados:**

    "Ou, se você se sente pronto para novos desafios, o mundo da tecnologia oferece inúmeras especializações fascinantes. Que tal explorar alguns desses caminhos?

    *   **Inteligência Artificial e Machine Learning:** Mergulhe em algoritmos de aprendizado, redes neurais, processamento de linguagem natural e visão computacional.
    *   **Desenvolvimento Mobile:** Aprenda a criar aplicativos para Android e iOS com tecnologias como React Native, Flutter ou linguagens nativas.
    *   **Cibersegurança:** Aprofunde-se em segurança de redes, análise de vulnerabilidades, criptografia e defesa contra ataques cibernéticos.
    *   **Cloud Computing Avançado:** Explore arquiteturas de nuvem, automação de infraestrutura e serviços especializados em AWS, Azure ou GCP.

    Estamos aqui para apoiar sua jornada contínua de aprendizado. Qual será seu próximo passo?"

---
