class PropElement:
    def __init__(self, element):
        self._element = element

    def __repr__(self):
        return f"render({self._element._module},{self._element._element},{{{self._element._props}}},[{self._element._children}], true)"
