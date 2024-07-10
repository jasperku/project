import os
import openai

# Web UI
import panel as pn
pn.extension()

panels = []

inp1 = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

dashboard = pn.Column(inp1, pn.Row(button_conversation))

# Serve
pn.template.FastListTemplate(
    site="Panel", title="Test Panel", main=[dashboard],
).servable()
