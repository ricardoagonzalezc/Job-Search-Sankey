import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["Applied Jobs (196)", "Rejected Job (44)", "No Answer (145)", "Interviews (7)", "Offer (1)", "Declined Offer (1)", "No Offer (6)"],
      color = "lightgray"
    ),
    link = dict(
      source = [0, 0, 0, 3, 3, 4],
      target = [1, 2, 3, 4, 6, 5],
      value = [44, 145, 7, 1, 6, 1], 

      color = ["rgba(250, 128, 114, 0.5)",
               "rgba(96, 125, 139, 0.65)", 
               "rgba(168, 208, 141, 0.65)",
               "rgba(255, 215, 0, 0.65)",
               "rgba(250, 128, 114, 0.5)",
               "rgba(255, 165, 0, 0.65)"]

  ))])

fig.update_layout(
    title_text="Job Application Process - Summer 2021<br><sub>May-Aug</sub>",
    font_size=12,
    height=550)
fig.show()


# Explanation of the flow used:
# Node 0 (Applied Jobs): 196 total applications
#   ├─> Node 1 (Rejected): 44 rejected
#   ├─> Node 2 (No Answer): 145 with no response
#   └─> Node 3 (Interviews): 7 interviews secured
#
# Node 3 (Interviews): 7 interviews
#   └─> Node 4 (Offer): 1 offer received
#
# Node 4 (Offer): 1 offer
#   └─> Node 5 (Declined Offer): 1 declined

#Sankey graphs can be used to visualize the proportional transfer of data, energy, materials or in this case job applications.


