import functools

class Controller:

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__connect_signals()

    def __connect_signals(self):
        buttons = self.__view.get_buttons()
        for text, btn in buttons.items():
            if text not in {'C', '='}:
                btn.clicked.connect(functools.partial(self.__build_expr, text))

        buttons['C'].clicked.connect(self.__view.clear_display)
        buttons['='].clicked.connect(self.__calc_result)


    def __build_expr(self, text):
        expression = self.__view.get_display_text() + text
        self.__view.set_display_text(expression)

    def __calc_result(self):
        result = self.__model.exec_expr(self.__view.get_display_text())
        self.__view.set_display_text(result)


        #comentario poara el github