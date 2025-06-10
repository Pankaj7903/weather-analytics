def suggest_chart(data_type, goal):
    if data_type == 'time_series' and goal == 'trend':
        return "Line Chart"
    elif data_type == 'numerical' and goal == 'distribution':
        return "Histogram with KDE"
    elif data_type == 'categorical' and goal == 'comparison':
        return "Bar Chart"
    elif data_type == 'numerical' and goal == 'correlation':
        return "Scatter Plot or Heatmap"
    elif data_type == 'multivariate' and goal == 'compare groups':
        return "Grouped Line Chart or Box Plot"
    return "Manual selection required"
def suggest_chart(data_type: str, goal: str) -> str:
    suggestions = {
        ('time_series', 'trend'): "Line Chart",
        ('numerical', 'distribution'): "Histogram + KDE",
        ('categorical', 'comparison'): "Bar Chart",
        ('numerical', 'correlation'): "Scatter Plot or Heatmap",
        ('multivariate', 'group comparison'): "Box Plot or Grouped Line Chart"
    }
    return suggestions.get((data_type, goal), "Manual chart recommendation required")
