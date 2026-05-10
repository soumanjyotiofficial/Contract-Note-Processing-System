import re
import json
import ast
#Stage 1 — The Sanitiser Function
def sanitize_llm_response(raw_text:str)-> str:
    """
    This remove the extra text and extract only json objects

    """
    text = raw_text.strip()
    text = re.sub(r'```(?:json)?',"",text).strip()
    start = text.find('{') #find the first opening {
    end_ = text.rfind('}') #find the last closing }
    if start == -1 or end_ ==-1:
        raise ValueError("No Json Object Found in LLM response")
    return text[start: end_+1]


def json_converter(input_)->dict:
    try:
        return json.loads(input_)
    except Exception as exp:
        try:
            return ast.literal_eval(input_)
        except Exception as e:
            print(f"Error while converting inputs into dict {exp}\n\n{e}")
            raise

