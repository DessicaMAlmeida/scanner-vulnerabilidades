# scanner-vulnerabilidades
Scanner de portas TCP em Python com Socket e Threading - Projeto de estudo para Pentest | Inspirado no Nmap
# **Obrigatório**
> ⚠️ Uso apenas ético e autorizado! Projeto para estudo de redes.

### 🛠️ Tecnologias utilizadas
| Tecnologia | Uso no projeto |
|---|---|
| Python 3 | Linguagem principal |
| Socket | Conexões TCP |
| Threading | Paralelização - 100 threads |
| Argparse | CLI --host, --portas |

### 🚀 Como testar no Windows
```bash
# Terminal 1 - cria porta fake
python -m http.server 8080

# Terminal 2 - testa seu scanner
python scanner.py --host 127.0.0.1 --portas 1-1000 --threads 100
