def tags(*tag_args):
    def decorator_tags(func):
        func.tags = tag_args
        return func
    return decorator_tags
