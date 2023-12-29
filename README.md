# DS-AI-Bot-Interviewer
This is AI Bot Interviewer. It helps to prepare the data science interviewers by asking quesions based on your selection perference. It will analyze the user answer and provide feedback and simplified answer to user.

Clone the git repository
```bash
git clone https://github.com/elavalasrinivasreddy/DS-AI-Bot-Interviewer.git
```
Change the directory
```bash
~$ cd
```
Create conda environment
```bash
conda create -n AI_Interviewer python=3.9
```
Activate the environment and install requirements
```bash
conda activate AI_Interviewer
python -m pip install -r requirements.txt
```
For GPU activation run the below commands 
```bash
conda install -c anaconda cudatoolkit
conda install -c anaconda cudnn
Download Pytorch by visiting https://pytorch.org/  {choose pip}
```
To check python is accessing cuda {True - We can use GPU}
```bash
import torch
print("torch.cuda.is_available")
```
To Run the Application
```bash
streamlit run app.py
```
#### Tech-stack
```bash
--Python
--Langchain
--Streamlit
--Meta Llama-2
--HuggingFace Transformers
```