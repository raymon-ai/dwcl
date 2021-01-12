# AUTO GENERATED FILE - DO NOT EDIT

dashWindowCloseListener <- function(id=NULL, status=NULL) {
    
    props <- list(id=id, status=status)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashWindowCloseListener',
        namespace = 'dwcl',
        propNames = c('id', 'status'),
        package = 'dwcl'
        )

    structure(component, class = c('dash_component', 'list'))
}
