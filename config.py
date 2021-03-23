
liveEvent = {
    'url': "https://www.betsson.com/api/sb/v1/competitions/liveEvents",
    'payload': {},
    'headers': {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.5',
        'accept-encoding': 'gzip, deflate',
        'content-type': 'application/json',
        'brandid': 'e123be9a-fe1e-49d0-9200-6afcf20649af',
        'marketcode': 'en',
        'x-obg-device': 'Desktop',
        'x-obg-channel': 'Web',
        'x-obg-country-code': 'PE',
        'cloudfront-viewer-country': 'PE',
        'correlationid': '31477eb1-5e6e-4920-9264-a4f607bfa59a',
        'x-obg-experiments': 'ssrClientConfiguration',
        'x-sb-identifier': 'LIVE_EVENTS_REQUEST',
        'x-sb-segment-guid': '6f239807-f21c-4b65-8bc3-a5640e1c27b7',
        'referer': 'https://www.betsson.com/en/sportsbook/live/football',
        'cache-control': 'max-age=0',
        'te': 'trailers',
        'cookie': 'OBG-MARKET=en; _gcl_au=1.1.359630968.1615780045; Acquisition_Status_Current=Prospect; Start_Acquisition=Prospect; Client_Status_Current=Existing Customer; Start_Client_Status=Existing Customer; VIQ_P1=1615780045128_1066172; _ga=GA1.2.1420253124.1615780049; _fbp=fb.1.1615780050807.2022575195; kppid_managed=kppidff_OAE_Hrbm; _hjid=ffdea14c-32dd-4cd6-ba93-2b4e62ffbabb; GAClientID_Cookie=1420253124.1615780049; CONSENT=%7B%22marketing%22%3A1%7D; GUID_Cookie=2a36e99d-a293-4633-9cde-a5cafcee882f; token=https%3A%2F%2Fwww.google.com%2F; affcode=hgjeap65; PartnerId=hgjeap65; OBG-LOBBY=sportsbook; Initdone=1; TrafficType=Other Traffic; Orientation=0; _gid=GA1.2.1990528585.1616376219; _hjTLDTest=1; _hjAbsoluteSessionInProgress=0; kppid=GA1.2.1420253124.1615780049; AffCookie=Missing AffCode; LoadAll=0; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=0; domain.viq=betsson; _gat_UA-49401878-1=1; _uetsid=3bc710208aad11eb87c1db0fdee36704; _uetvid=2807c380854111ebb4ece98e20bb6530; OBG-MARKET=pe'
    }
}


def eventMatch(eventId):
    return {
        'url': f"https://www.betsson.com/api/sb/v1/widgets/view/v1?configurationKey=sportsbook.event&eventId={eventId}",
        'payload': {},
        'headers': {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0",
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.5",
            "accept-encoding": "gzip, deflate",
            "content-type": "application/json",
            "brandid": "e123be9a-fe1e-49d0-9200-6afcf20649af",
            "marketcode": "en",
            "x-obg-device": "Desktop",
            "x-obg-channel": "Web",
            "x-obg-country-code": "PE",
            "cloudfront-viewer-country": "PE",
            "correlationid": "3b25c0ab-d252-4346-aa4e-39e1a14516d0",
            "x-obg-experiments": "ssrClientConfiguration",
            "x-sb-identifier": "SPORTSBOOK_EVENT_WIDGET_REQUEST",
            "x-sb-segment-guid": "6f239807-f21c-4b65-8bc3-a5640e1c27b7",
            "referer": f"https://www.betsson.com/en/sportsbook/live/football?eventId={eventId}",
            "te": "trailers",
            "cookie": "OBG-MARKET=en; _gcl_au=1.1.359630968.1615780045; Acquisition_Status_Current=Prospect; Start_Acquisition=Prospect; Client_Status_Current=Existing Customer; Start_Client_Status=Existing Customer; VIQ_P1=1615780045128_1066172; _ga=GA1.2.1420253124.1615780049; _fbp=fb.1.1615780050807.2022575195; kppid_managed=kppidff_OAE_Hrbm; _hjid=ffdea14c-32dd-4cd6-ba93-2b4e62ffbabb; GAClientID_Cookie=1420253124.1615780049; CONSENT=%7B%22marketing%22%3A1%7D; GUID_Cookie=2a36e99d-a293-4633-9cde-a5cafcee882f; token=https%3A%2F%2Fwww.google.com%2F; affcode=hgjeap65; PartnerId=hgjeap65; _gid=GA1.2.1990528585.1616376219; OBG-LOBBY=sportsbook; Orientation=0; _hjTLDTest=1; kppid=GA1.2.1420253124.1615780049; Initdone=1; TrafficType=Other Traffic; AffCookie=Missing AffCode; LoadAll=0; domain.viq=betsson; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; _hjIncludedInSessionSample=0; _gat_UA-49401878-1=1; _uetsid=3bc710208aad11eb87c1db0fdee36704; _uetvid=2807c380854111ebb4ece98e20bb6530",
        }
    }
