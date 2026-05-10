
import config as conf
from visionengine import VisionEngine_
import glob
from openai import OpenAI
import pandas as pd
from utils import sanitize_llm_response, json_converter
#Connecting client
client = OpenAI(api_key="<You API>", base_url="<BASE URL>")

#Loading Prompt and File paths
prompt = open("E:\\Quant_fin\\1_Agentic_Ai\\Contract_Processer\\contract_note_system_prompt.txt", "r", encoding="utf-8").read()
paths = glob.glob("E:\\Quant_fin\\1_Agentic_Ai\\Contract_Processer\\Decrypted_Document\\*PDF")

#Level 1 processing
#18
extracteddocument = VisionEngine_(model=conf.NVIDAI_VISION_INSTRUCT_MODEL,API_URL=conf.NVIDAI_VISION_INSTRUCT_URL,dpi=200, img_format="jpeg",save_image=False,prompt=prompt,path=paths[1], API=conf.NVIDIA_API_KEY)._extract_document()
print("20")
print(extracteddocument.keys())
print(extracteddocument['raw_response'])
with open("response.txt","w") as f: 
    f.write("".join(a for a in extracteddocument['raw_response']))


content = json_converter(sanitize_llm_response(extracteddocument['raw_response']))
#pd.DataFrame([content['Client_Detail']])
if type(content)==tuple:
    content = content[0]
for a in content.keys():
    print(a)
    if a == "Equity_Segment":
        df = pd.DataFrame(content[a])
        
        df.round(4)
        df.to_excel(f"{a}.xlsx", index=False)
    elif a == "Trade_Annexure":
        df = pd.DataFrame(content[a])
        
        df.round(4)
        df.to_excel(f"{a}.xlsx", index=False)
    else:
        df = pd.DataFrame([content[a]])
        df.round(4)
        df.to_excel(f"{a}.xlsx",index=False)  
