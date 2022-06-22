import matplotlib.pyplot as plt
import max_line_calc

graphs = []
points = []
plot_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
plot_colors_n = -1
mpl_connection = True


def cycle_color():
    global plot_colors_n

    if plot_colors_n < len(plot_colors):
        plot_colors_n += 1
    else:
        plot_colors_n = 0
    return plot_colors_n


def onclick(event):
    global points, graphs, mpl_connection, none_once

    point = (event.xdata, event.ydata)
    if None in point:
        if point == (None, None):
            if none_once:
                fig.canvas.mpl_disconnect(cid)
                mpl_connection = False
                #plt.cla()
                ax.scatter([0, x_range], [0, y_range])
                second_module()
            else:
                none_once = True
                if len(points) != 0:
                    graphs.append(points)
                points = []
    elif (x_range >= point[0] >= 0) and (y_range >= point[1] >= 0):
        if len(points) == 0:
            cycle_color()
            points.append(point)
        elif point[0] > points[-1][0]:
            points.append(point)
            ax.plot([points[-1][0], points[-2][0]], [points[-1][1], points[-2][1]], plot_colors[plot_colors_n])
            fig.canvas.draw()
            # fig.canvas.flush_events()
        none_once = False


def range_input_process(range_input):
    range_input = range_input.split(',')
    try:
        return float(range_input[0].strip(' ')), float(range_input[1].strip(' '))
    except ValueError:
        print('Invalid value!')
        return None, None
    except IndexError:
        print('Enter two numbers!')
        return None, None


def begin(range_input):
    global cid, fig, x_range, y_range, ax, none_once

    x_range, y_range = range_input_process(range_input)
    if (x_range, y_range) == (None, None):
        return 1
    else:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter([0, x_range], [0, y_range])
        print('Click on the plot to make point entries.\
               \nClick outside of the plot once to make another graph entry,\
               \nand click twice to quit point entry mode and begin the calculation.')
        none_once = False
        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        plt.grid()
        plt.show()
        return 0


def second_module():
    global graphs, y_range
    x_processed = []
    y_processed = []

    processed_graph = max_line_calc.calc_max_line(graphs, x_range)

    #if (processed_graph[0][0] != 0) and (processed_graph[0][1] != 0):
    #    x_processed.append(0)
    #    y_processed.append(0)
    #    x_processed.append(processed_graph[0][0])
    #    y_processed.append(0)

    for p in processed_graph:
        x_processed.append(p[0])
        y_processed.append(p[1])
    ax.plot(x_processed, y_processed, '#000000')
    fig.canvas.draw()
    print('Process successfully finished!')


if __name__ == '__main__':
    ###
    #print(max_line_calc.calc_max_line([1], 1))
    ###

    while begin(input('Enter the maximum x coordinate and the maximum y coordinate.\
                     \nSeparate the values with a \",\".\n  ')) != 0:
        pass
