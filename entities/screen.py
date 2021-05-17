class Screen:
    mode = False
    matrix_x_y = [10, 10]
    agent_x_y = [0, 0]
    goal_x_y = [5, 5]
    hurdle_rate = 1
    learning_rate = 0.8

    square_size = 19

    window_height = 850
    window_width = 650

    def resize(row, column):
        Screen.resize_square(row, column)
        Screen.resize_window(row, column)

    def resize_square(row, column):
        if row < column:
            Screen.square_size = (int)((800)/column)
        else:
            Screen.square_size = (int)((800)/row)

    def resize_window(row, column):
        Screen.window_height = Screen.square_size * row
        Screen.window_width = Screen.square_size * column

    def reset_window_size():
        Screen.window_width = 650
        Screen.window_height = 850
