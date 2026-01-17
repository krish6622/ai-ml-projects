from fastapi import FastAPI
from pydantic import BaseModel
from app.mcp_router import route_tool
from app.memory.conversation import add_memory

app=FastAPI(title="MCP GenAI Insurance System")

class MCPRequest(BaseModel):
    tool:str
    input:str
@app.post("/mcp/run")
def run_mcp(req:MCPRequest):
    add_memory("user",req.input)
    result=route_tool(req.tool,req.input)
    add_memory("assistant",result)

    return{
        "tool_used":req.tool,
        "response":result
    }