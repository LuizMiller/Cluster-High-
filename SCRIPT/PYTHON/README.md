# 🐍 Scripts Python - Cluster High

Esta pasta contém scripts auxiliares escritos em **Python**, desenvolvidos para suportar a automação de testes, captura e análise de imagens e comunicação com dispositivos externos no projeto **Cluster High**.

---

## 📜 Descrição dos Arquivos

### 🔌 `COM_Config`
- **Função:** Gerencia a **comunicação serial** com dispositivos externos.
- **Aplicação:** Estabelece conexão e troca de dados via porta COM.

---

### 📸 `Capture_Image`
- **Função:** Realiza a **configuração da câmera via IP** e captura de imagem.
- **Comunicação:** Utiliza **Wi-Fi** como canal de comunicação com o dispositivo.

---

### 🧠 `Compare_Image`
- **Função:** Compara a imagem capturada com um **banco de dados de imagens de referência**.
- **Tecnologia:** Utiliza redes neurais **CLIP (OpenAI)** para inferência visual.
- **Saída:** Adiciona o resultado da análise ao relatório do CANoe com status **PASS/FAIL**.

---

### 🔤 `OCR_Detection`
- **Função:** Detecta e extrai **texto presente na imagem** utilizando OCR.
- **Saída:** Após análise, gera um registro no relatório CANoe com status **PASS/FAIL**.

---

## 👤 Autor

**Luiz Miller França**  
Desenvolvedor de Testes | Software Automotivo

---

