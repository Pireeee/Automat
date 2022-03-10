from Display import Display

def test():#appele la class Display pour pouvoir la tester
    var=Display()
    var.generate_tuples_node()
    var.draw_graph()

test()