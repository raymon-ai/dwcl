
module Dwcl
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("dashwindowcloselistener.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dwcl",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dwcl.min.js",
    external_url = "https://unpkg.com/dwcl@0.0.1/dwcl/dwcl.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dwcl.min.js.map",
    external_url = "https://unpkg.com/dwcl@0.0.1/dwcl/dwcl.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
