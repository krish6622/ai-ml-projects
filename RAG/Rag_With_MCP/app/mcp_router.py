from app.tools.rag_tool import rag_insurance

def route_tool(tool_name:str,input_text:str):
    if tool_name=="rag_insurance_qa":
        return rag_insurance(input_text)
    raise ValueError("Unknown tool")


    
