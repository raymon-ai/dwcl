# AUTO GENERATED FILE - DO NOT EDIT

dashWindowCloseListener <- function(id=NULL, label=NULL, value=NULL) {
    
    props <- list(id=id, label=label, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashWindowCloseListener',
        namespace = 'dwcl',
        propNames = c('id', 'label', 'value'),
        package = 'dwcl'
        )

    structure(component, class = c('dash_component', 'list'))
}
