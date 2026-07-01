class MetadataFilter:

    def filter(self, catalog, context):

        filtered = catalog

        # Filter by Job Level
        if context.get("job_level"):
            filtered = [
                item for item in filtered
                if context["job_level"] in item.get("job_levels", [])
            ]

        # Filter by Remote
        if context.get("remote") is True:
            filtered = [
                item for item in filtered
                if item.get("remote") == "yes"
            ]

        # Filter by Adaptive
        if context.get("adaptive") is True:
            filtered = [
                item for item in filtered
                if item.get("adaptive") == "yes"
            ]

        return filtered