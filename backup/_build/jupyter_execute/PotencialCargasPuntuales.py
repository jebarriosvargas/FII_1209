#!/usr/bin/env python
# coding: utf-8

# # Potencial de cargas puntuales

# En el gráfico siguiente se ilustran las equipontenciales del potencial debido a tres cargas puntuales, considerando como referencia que el pontencial en el infinito es igual a cero.
# 
# \begin{align}
# \Delta V_{\infty\to P} = V(P)-V(\infty)
# \end{align}
# donde $V(\infty)=0$ y 
# 
# \begin{align}
# V(P) = \frac{k_e q_1}{r_{1\to P}}+\frac{k_e q_2}{r_{2\to P}}+\frac{k_e q_3}{r_{3\to P}}
# \end{align}

# In[1]:


from pylab import *
import plotly.graph_objects as go


# In[2]:


Cargas = {
    0:{'q':-1e-9,'x': 1.0,'y': 1.0,'z':0.0},
    1:{'q':-1e-9,'x':-1.0,'y':-1.0,'z':0.0},
    2:{'q':+2e-9,'x': 1.0,'y':-1.0,'z':0.0}
}


# In[3]:


N = 60*1J
xmin,xmax = -2.2,2.2
ymin,ymax = -2.2,2.2
zmin,zmax = -2.2,2.2
X,Y,Z = mgrid[xmin:xmax:N,ymin:ymax:N,zmin:zmax:N]


# In[4]:


ke = 9e9
V  = zeros_like(X)
for key in Cargas:
    xC = Cargas[key]['x']
    yC = Cargas[key]['y']
    zC = Cargas[key]['z']
    q  = Cargas[key]['q']
    V += ke*q/sqrt( (X-xC)*(X-xC)                   +(Y-yC)*(Y-yC)                   +(Z-zC)*(Z-zC))


# In[5]:


DATA = [ go.Volume(x=X.flatten(),
                   y=Y.flatten(),
                   z=Z.flatten(),
                   value=V.flatten(),
                   isomin=-10.0,
                   isomax= 10,
                   opacity=0.1,
                   surface_count=20,
                   colorscale='RdBu_r'),
        go.Scatter3d(x=[Cargas[0]['x']],
                     y=[Cargas[0]['y']],
                     z=[Cargas[0]['z']],
                     mode='markers',
                     marker=dict(color="blue"),
                     showlegend=False),
        go.Scatter3d(x=[Cargas[1]['x']],
                     y=[Cargas[1]['y']],
                     z=[Cargas[1]['z']],
                     mode='markers',
                     marker=dict(color="blue"),
                     showlegend=False),
        go.Scatter3d(x=[Cargas[2]['x']],
                     y=[Cargas[2]['y']],
                     z=[Cargas[2]['z']],
                     mode='markers',
                     marker=dict(color="red"),
                     showlegend=False),]


# In[6]:


fig = go.Figure(data=DATA) 
fig.show()


# In[ ]:




