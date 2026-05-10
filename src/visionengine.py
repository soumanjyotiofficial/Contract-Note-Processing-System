from pdftoencodding import PDF2IMAGECONVERTER,ImageMerger
import config as conf
import requests as req
import pdb


class VisionEngine:
    def __init__(self,model,API_URL,API, path:str,  prompt:str,dpi:int=100,save_image:bool=False,img_format:str="png",save_image_to:str=".\\temp_image"):
        self.model= model
        self.dpi=dpi
        self.path = path
        self.prompt = prompt
        self.save_image = save_image
        self.img_format = img_format
        self.save_image_to = save_image_to
        self.API_URL  =API_URL
        self.API = API

    def extract_document(self):
    
        pdf2encodeing = PDF2IMAGECONVERTER(
            path=self.path,
            dpi=self.dpi,
            img_format=self.img_format,
            save_image=self.save_image,
            save_image_to=self.save_image_to
            ).pdf2image()
        
        raw_response = {"raw_response":[], "finalpath":pdf2encodeing["finalpath"]}
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": None
                }
            ],
            "temperature": 0.1,
            "top_p": 0.7,
            "max_tokens": 3000,
            "stream": False
        }

        for emb in pdf2encodeing['embeddings']:
            payload['messages'][0]['content'] = [{"type": "text","text": self.prompt},
                    
                    {"type": "image_url","image_url": {"url": f"data:image/{pdf2encodeing['format']};base64,{emb}"}}
                                                        ]
            
            response =  self._get_image_response(payload=payload)
            print("STATUS:", response.status_code)
            
            if response.status_code != 200:
                print("FULL ERROR:", response.text)
                raw_response['raw_response'].append({"FULL ERROR":response.text})


            result = response.json()

            raw = result["choices"][0]["message"]["content"]
            raw_response["raw_response"].append(raw)
            

            
            
            
        return raw_response
    
    def _extract_document(self):
    
        pdf2encodeing = PDF2IMAGECONVERTER(
            path=self.path,
            dpi=self.dpi,
            img_format=self.img_format,
            save_image=self.save_image,
            save_image_to=self.save_image_to
            ).pdf2image()
        
        raw_response = {"raw_response":[], "finalpath":pdf2encodeing["finalpath"]}
        content = []
        
        content.append({"type":"text","text": self.prompt})
        content.append({"type": "image_url","image_url": {"url": f"data:image/{pdf2encodeing['format']};base64,{pdf2encodeing['embeddings'][0]}"}})
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "temperature": 0.1,
            "top_p": 0.7,
            "max_tokens": 3000,
            "stream": False
        }


        
        response =  self._get_image_response(payload=payload)
        
        print("STATUS:", response.status_code)
        
        if response.status_code != 200:
            print("FULL ERROR:", response.text)
            raw_response['raw_response'].append({"FULL ERROR":response.text})


        result = response.json()
        print(result)
        raw = result["choices"][0]["message"]["content"]
        print(raw)
        raw_response["raw_response"].append(raw)
        

        
            
            
        return raw_response
    
    
    
    def _get_image_response(self,payload):
        len(payload["messages"])
        headers = {"Authorization": f"Bearer {self.API}","Content-Type": "application/json"}
        
        response = req.post(self.API_URL, headers=headers, json=payload, timeout=120)
        print("Ok")
        return response

        


class VisionEngine_:
    def __init__(self,model,API_URL,API, path:str,  prompt:str,dpi:int=100,save_image:bool=False,img_format:str="png",save_image_to:str=".\\temp_image"):
        self.model= model
        self.dpi=dpi
        self.path = path
        self.prompt = prompt
        self.save_image = save_image
        self.img_format = img_format
        self.save_image_to = save_image_to
        self.API_URL  =API_URL
        self.API = API
        self.payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": None
                }
            ],
            "temperature": 0.0,
            "top_p": 0.7,
            "max_tokens": 3000,
            "stream": False
        }

    def extract_document(self):
    
        pdf2encodeing = PDF2IMAGECONVERTER(
            path=self.path,
            dpi=self.dpi,
            img_format=self.img_format,
            save_image=self.save_image,
            save_image_to=self.save_image_to
            ).pdf2image()
        pdf2encodeing = ImageMerger(self.path,self.dpi, self.img_format,self.save_image, self.save_image_to).run()
        return None
    
    def _extract_document(self):
        pdf2encodeing = PDF2IMAGECONVERTER(
            path=self.path,
            dpi=self.dpi,
            img_format=self.img_format,
            save_image=self.save_image,
            save_image_to=self.save_image_to
            ).pdf2image()
        
        pdf2encodeing = ImageMerger(self.path,self.dpi, self.img_format,self.save_image, self.save_image_to).run()
        content = []
        content.append({"type":"text","text": self.prompt})
        content.append({"type": "image_url","image_url": {"url": f"data:image/{self.img_format};base64,{pdf2encodeing['merged_encoded']}"}})
        payload = {
            "model": self.model,"messages": [{"role": "user","content": content}],"temperature": 0.1,"top_p": 0.7,"max_tokens": 3000,"stream": False,

            }
        payload.update({ "presence_penalty": 0,"repetition_penalty": 1,"chat_template_kwargs": {"enable_thinking":True}})
        #191
        raw_response = {}
        response =  self._get_image_response(payload=payload)
        print("STATUS:", response.status_code)
        if response.status_code != 200:
            print("FULL ERROR:", response.text)
            raw_response['raw_response'].append({"FULL ERROR":response.text})
        result = response.json()
        
        raw = result["choices"][0]["message"]["content"]
        print(raw)
        raw_response["raw_response"]  = raw
        return raw_response
    
    
    
    def _get_image_response(self,payload):
        
        headers = {"Authorization": f"Bearer {self.API}","Content-Type": "application/json"}
        print("Ok 210")
        response = req.post(self.API_URL, headers=headers, json=payload, timeout=360)
        print("Ok")
        return response



class VisionPostEnging:
    def __init__(self, client, prompt, user_input):
        self.client = client
        self.prompt = prompt
        self.user_input  = user_input
    
    def postprocesser(self):
        text_client = self.client.chat.completions.create(
            model=conf.DEFAULT_MODEL,
            messages=[
                {"role":"system","content":self.prompt},
                {"role":"user","content":"Extract the structured response:\n".join(a for a in self.prompt)}

            ],
            temperature=0.1,max_tokens=2000
        )
        return text_client