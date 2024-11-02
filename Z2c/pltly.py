import random

from cluster import Cluster_C
import plotly.graph_objects as go

def plotScatter(list_of_clusters):
    x_axis = []
    y_axis = []
    centroids_x = []
    centroids_y = []
    cluster_id = []
    id = 0

    for cl in list_of_clusters:
        id += 1
        centroids_x.append(cl.center.x)
        centroids_y.append(cl.center.y)
        for tp_pt in cl.contents:
            x_axis.append(tp_pt[0])
            y_axis.append(tp_pt[1])
            cluster_id.append(id)

    # Assign random colors for each cluster
    unique_ids = set(cluster_id)
    colors = {cid: f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})' for cid in
              unique_ids}

    # Initialize Plotly figure
    fig = go.Figure()

    # Plot each cluster's points with its color
    for cid in unique_ids:
        cid_x = [x_axis[i] for i in range(len(x_axis)) if cluster_id[i] == cid]
        cid_y = [y_axis[i] for i in range(len(y_axis)) if cluster_id[i] == cid]

        fig.add_trace(go.Scatter(
            x=cid_x,
            y=cid_y,
            mode='markers',
            marker=dict(color=colors[cid], opacity=0.2),
            name=f'Cluster {cid}',
        ))

    # Plot centroids as larger, distinct markers
    fig.add_trace(go.Scatter(
        x=centroids_x,
        y=centroids_y,
        mode='markers',
        marker=dict(color='black', size=10, symbol='x'),
        name='Centroids'
    ))

    # Update layout
    fig.update_layout(title="Aglomerativne klustrovanie / centroid",
                      xaxis_title='X axis',
                      yaxis_title='Y axis')

    fig.show()