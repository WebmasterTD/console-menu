from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *


def main():
    format = MenuFormatBuilder().set_border_style(UnicodeLightBorderStyle()).set_prompt(u"\u27EB")
    menu = ConsoleMenu("Root Menu", "Root Menu Subtitle", formatter=format)
    item1 = MenuItem("Item 1", menu)
    function_item = FunctionItem("Fun item", raw_input, ["Enter an input: "])
    command_item = CommandItem("Command", 'sh -c \'echo "this is a shell. Press enter to continue."; read\'')
    submenu = SelectionMenu(["item1", "item2", "item3"], title="Selection Menu", formatter=format)
    submenu_item = SubmenuItem("Submenu item", submenu=submenu)
    submenu_item.set_menu(menu)
    submenu_2 = ConsoleMenu("Submenu Title", "Submenu subtitle", formatter=format)
    function_item_2 = FunctionItem("Fun item", raw_input, ["Enter an input"])
    item2 = MenuItem("Another Item")
    submenu_2.append_item(function_item_2)
    submenu_2.append_item(item2)
    submenu_item_2 = SubmenuItem("Another submenu", submenu=submenu_2)
    submenu_item_2.set_menu(menu)
    menu.append_item(item1)
    menu.append_item(function_item)
    menu.append_item(command_item)
    menu.append_item(submenu_item)
    menu.append_item(submenu_item_2)
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
