# AUTO GENERATED FILE - DO NOT EDIT

export dashwindowcloselistener

"""
    dashwindowcloselistener(;kwargs...)

A DashWindowCloseListener component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `status` (String; optional): The status of the window. Mounted or closing.
"""
function dashwindowcloselistener(; kwargs...)
        available_props = Symbol[:id, :status]
        wild_props = Symbol[]
        return Component("dashwindowcloselistener", "DashWindowCloseListener", "dwcl", available_props, wild_props; kwargs...)
end

