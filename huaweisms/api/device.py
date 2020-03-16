from huaweisms.api.common import (
    post_to_url,
    get_from_url,
    ApiCtx,
)


def information(ctx):
    # type: (ApiCtx) -> dict
    url = "{}/device/information".format(ctx.api_base_url)
    return get_from_url(url, ctx)


def basic_information(ctx):
    # type: (ApiCtx) -> dict
    url = "{}/device/information".format(ctx.api_base_url)
    return get_from_url(url, ctx)


def reboot(ctx):
    # type: (ApiCtx) -> dict
    """
    Reboots the modem.
    """

    url = '{}/device/control'.format(ctx.api_base_url)
    headers = {
        '__RequestVerificationToken': ctx.token,
    }

    payload = '<?xml version: "1.0" encoding="UTF-8"?><request><Control>1</Control></request>'
    return post_to_url(url, payload, ctx, additional_headers=headers)

def net1800(ctx):
    # type: (ApiCtx) -> dict
    """
    Reboots the modem.
    """

    url = '{}/net/net-mode'.format(ctx.api_base_url)
    headers = {
        '__RequestVerificationToken': ctx.token,
    }

    payload = '<?xml version: "1.0" encoding="UTF-8"?><request><NetworkMode>03</NetworkMode><NetworkBand>3FFFFFFF</NetworkBand><LTEBand>4</LTEBand></request>'
    return post_to_url(url, payload, ctx, additional_headers=headers)

def net2600(ctx):
    # type: (ApiCtx) -> dict
    """
    Reboots the modem.
    """

    url = '{}/net/net-mode'.format(ctx.api_base_url)
    headers = {
        '__RequestVerificationToken': ctx.token,
    }

    payload = '<?xml version: "1.0" encoding="UTF-8"?><request><NetworkMode>03</NetworkMode><NetworkBand>3FFFFFFF</NetworkBand><LTEBand>2000000000</LTEBand></request>'
    return post_to_url(url, payload, ctx, additional_headers=headers)


def netall(ctx):
    # type: (ApiCtx) -> dict
    """
    Reboots the modem.
    """

    url = '{}/net/net-mode'.format(ctx.api_base_url)
    headers = {
        '__RequestVerificationToken': ctx.token,
    }

