from dialogs_forked import checkboxlist_dialog


class Ui:

    @staticmethod
    def select_apps(apps):
        results = checkboxlist_dialog(
            title="Выберите приложения для удаления",
            text="Внимание! Удаление системных приложений может нарушить работоспособность устройства!",
            values=list(map(lambda x: (x, x), apps))
        ).run()
        return results

    @staticmethod
    def confirm_to_delete(apps, pre_selected=False):
        results = checkboxlist_dialog(
            title="Для подтверждения удаления еще раз выберите приложения",
            text="Внимание! Данные приложений будут потеряны",
            values=list(map(lambda x: (x, x), apps)),
            initial_selected=apps if pre_selected else []
        ).run()
        return results
