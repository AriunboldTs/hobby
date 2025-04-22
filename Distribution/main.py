from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse , FileResponse, RedirectResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

import io
import numpy as np
import matplotlib.pyplot as plt

from template import *
from calculator import Poisson, Geometric, Binomial, Normal


app = FastAPI()

@app.get("/", response_class=HTMLResponse) 
async def read_html():
    html_content = tpl_run(tpl_home)
    return HTMLResponse(content=html_content)

# Poisson - Start  -------------------------------------------->

@app.get("/poisson/")
async def read_item():
    return RedirectResponse( "/poisson/3/4/5")

@app.get("/poisson/{P_x}/{P_a}/{P_b}", response_class=HTMLResponse)
async def read_item(P_x:str , P_a:str, P_b:str):
    html_content = tpl_run(tpl_poisson + tpl_return.format(Poisson(int(P_x), int(P_a), int(P_b))))
    return HTMLResponse(content=html_content)

@app.post("/poisson/")
async def poisson(P_x: str = Form(), P_a: str = Form(), P_b: str = Form()):

    html_content =  tpl_run(tpl_poisson + tpl_return.format(Poisson(int(P_x), int(P_a), int(P_b))) + tpl_image.format(int(P_x)))
    return HTMLResponse(content=html_content)

@app.get("/figure/{P_x}", )
async def figure(P_x:str):
    x = float(P_x)
    fig, ax = plt.subplots() 
    data = np.random.poisson(x, 1000)
    plt.hist(data, bins=range(min(data), max(data) + 1), alpha=0.6, color='b', edgecolor='black', density=True)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0) 
    return StreamingResponse(buf, media_type="image/png")

# Poisson - END -------------------------------------------->

# Geometric - Start ---------------------------------------->

@app.get("/geometric/")
async def read_item():
    return RedirectResponse( "/geometric/1/5/5")

@app.get("/geometric/{P_p}/{P_x}/{P_a}", response_class=HTMLResponse)
async def read_item(P_p: str, P_x: str, P_a: str):
    
    html_content = tpl_header + tpl_geometric + tpl_return.format(Geometric(float(P_p), int(P_x), int(P_a))) + tpl_footer
    return HTMLResponse(content=html_content)

@app.post("/geometric/")
async def geometric(P_p: str = Form(), P_x:str = Form(), P_a:str = Form()):
    html_content = tpl_run(tpl_geometric + tpl_return.format(Geometric(float(P_p), int(P_x), int(P_a))) + tpl_geo_image.format(float(P_p)))
    return HTMLResponse(content = html_content)

@app.get("/figure_geo/{P_p}", )
async def figure_geo(P_p:str):
    p = float(P_p) 
    size = 10000  

    fig, ax = plt.subplots()
    data = np.random.geometric(p, size)

    plt.hist(data, bins=range(1, max(data) + 1), color='b', edgecolor='black', alpha=0.7, density=True)

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")
        
# Geometric - End -------------------------------------->

# Binomial - Start -------------------------------------> 

@app.get("/binomial/")
async def read_item():
    return RedirectResponse( "/binomial/20/1/5/5")

@app.get("/binomial/{P_n}/{P_p}/{P_a}/{P_b}", response_class=HTMLResponse)
async def read_item(P_n:str, P_p:str, P_a:str, P_b:str):
    
    html_content = tpl_run(tpl_binomial + tpl_return.format(Binomial(int(P_n), int(P_p), int(P_a), int(P_b))))
    return HTMLResponse(content=html_content)

@app.post("/binomial/")
async def binomial(P_n:str = Form(), P_p:str = Form(), P_a:str = Form(), P_b:str = Form()):
    html_content = tpl_run(tpl_binomial + tpl_return.format(Binomial(int(P_n), float(P_p), int(P_a), int(P_b))) + tpl_bin_image.format(int(P_n), float(P_p)))
    return HTMLResponse(content = html_content)  

@app.get("/figure_bin/{P_n}/{P_p}", )
async def figure_bin(P_n:str, P_p:str):
    n = int(P_n) 
    p = float(P_p)
    size = 10000 
    fig, ax = plt.subplots()
    data = np.random.binomial(n, p, size)

    plt.hist(data, bins=range(n + 2), color='b', alpha=0.7, edgecolor='black', density=True)

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0) 
    return StreamingResponse(buf, media_type="image/png")          

# Binomial - End --------------------------------------->

# Normal - Start ---------------------------------------->

@app.get("/normal/")
async def read_item():
    return RedirectResponse( "/normal/0/1/1/1")

@app.get("/normal/{P_mu}/{P_sygma}/{P_a}/{P_b}", response_class=HTMLResponse)
async def read_item(P_mu:str, P_sygma:str, P_a:str, P_b:str ):
    html_content = tpl_run(tpl_normal + tpl_return.format(Normal(int(P_mu), int(P_sygma), int(P_a), int(P_b))))
    
    return HTMLResponse(content=html_content)

@app.post("/normal/")
async def normal(P_mu:str = Form(), P_sygma:str = Form(), P_a:str = Form(), P_b:str = Form()):
    html_content = tpl_run(tpl_normal + tpl_return.format(Normal(int(P_mu), float(P_sygma), int(P_a), int(P_b))) + tpl_nor_image.format(int(P_mu), int(P_sygma)))
    return HTMLResponse(content = html_content)

@app.get("/figure_nor/{P_mu}/{P_sygma}", )
async def figure_nor(P_mu:str, P_sygma:str):

    mean = int(P_mu)  
    std_dev = int(P_sygma)
    size = 10000 
    fig, ax = plt.subplots()
    data = np.random.normal(mean, std_dev, size)

    plt.hist(data, bins=50, color='b', edgecolor='black', density=True)

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png") 

    # Normal - End ------------------------------------------->
