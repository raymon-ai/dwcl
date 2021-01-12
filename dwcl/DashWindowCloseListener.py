# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashWindowCloseListener(Component):
    """A DashWindowCloseListener component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- status (string; optional): The status of the window. Mounted or closing."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, status=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'status']
        self._type = 'DashWindowCloseListener'
        self._namespace = 'dwcl'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'status']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashWindowCloseListener, self).__init__(**args)
