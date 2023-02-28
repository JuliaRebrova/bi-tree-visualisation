import plotly.graph_objects as go

class TreeDrawer:
    def __init__(self, root):
        self.root = root
        self.x = 0
        self.y = 0
        self.Xe = []
        self.Ye = []
        self.Xn = []
        self.Yn = []
        self.labels = []
        self._get_coor(self.root, self.x, self.y)

    def _fulfil_lists(self, data):
        self.Xe.extend([data['root'][0], data['left'][0], None, data['root'][0], data['right'][0], None])
        self.Ye.extend([data['root'][1], data['left'][1], None, data['root'][1], data['right'][1], None])
        self.Xn.extend([data['root'][0], data['left'][0], data['right'][0]])
        self.Yn.extend([data['root'][1], data['left'][1], data['right'][1]])
        self.labels.extend([data['root'][2], data['left'][2], data['right'][2]])

    def _get_coor(self, root, x, y, counter = 100):
        data = {}
        coef = counter/2
    #     if root:
        data["root"] = [x,y,root.data]
        if root.left:
            data["left"] = [x-coef, y-coef, root.left.data]
        else:
            data["left"] = [None, None, None]
        if root.right:
            data["right"] = [x+coef, y-coef, root.right.data]
        else:
            data["right"] = [None, None, None]
        self._fulfil_lists(data)
    
        if root.left:
            _x = x-coef
            _y = y-coef
            self._get_coor(root.left, _x, _y, coef)
            
        if root.right:
            x_ = x+coef
            y_ = y - coef
            self._get_coor(root.right, x_, y_,coef)

    def _make_annotations(self, Xn, Yn, labels, font_size=12, font_color='rgb(250,250,250)'):
        annotations = []
        for k in range(len(labels)):
            annotations.append(
                dict(
                    text=labels[k], # or replace labels with a different list for the text within the circle
                    x=Xn[k], 
                    y=Yn[k],
                    xref='x1', yref='y1',
                    font=dict(color=font_color, size=font_size),
                    showarrow=False)
            )
        return annotations

    def show_plot(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.Xe,
                        y=self.Ye,
                        mode='lines',
                        line=dict(color='rgb(210,210,210)', width=1),
                        hoverinfo='none'
                        ))
        fig.add_trace(go.Scatter(x=self.Xn,
                        y=self.Yn,
                        mode='markers',
                        name='bla',
                        marker=dict(symbol='circle-dot',
                                        size=30,
                                        color='#6175c1',    #'#DB4551',
                                        line=dict(color='rgb(50,50,50)', width=1)
                                        ),
                        text=self.labels,
                        hoverinfo='text',
                        opacity=0.8
                        ))

        axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
                    zeroline=False,
                    showgrid=True,
                    showticklabels=False,
                    )

        fig.update_layout(title= 'Binary tree',
                    annotations=self._make_annotations(self.Xn, self.Yn, self.labels),
                    font_size=12,
                    showlegend=False,
                    xaxis=axis,
                    yaxis=axis,
                    margin=dict(l=40, r=40, b=85, t=100),
                    hovermode='closest',
                    plot_bgcolor='rgb(248,248,248)'
                    )
        fig.show()
