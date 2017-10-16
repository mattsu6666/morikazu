from lxml import html

def get_target_count(page, target_param):
    root = html.fromstring(page)
    tr = root.xpath('//table[@id="dataListSummary"]/*/tr[@data-record="rc_all"]')

    return tr[0].find('./td[@class="banner firstCol"]').text_content()
