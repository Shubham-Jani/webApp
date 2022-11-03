from django_components import component


@component.register("note")
class Navbar(component.Component):
    template_name = "note/note.html"

    def get_context_data(self, note_data):
        return {
            "note": note_data
        }
