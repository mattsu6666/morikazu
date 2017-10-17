from lxml import html


def get_target_count(page, target_param):
    """
    GUILEサイトからクローリングした値を取得し返す

    :param page: 対象のHTMLページ
    :param target_param: 取得したい値のカラム名
    :return: 取得した値
    """
    root = html.fromstring(page)
    tr = root.xpath('//table[@id="dataListSummary"]/*/tr[@data-record="rc_all"]')

    if target_param == 'imp':
        return int(tr[0].find('./td[3]').text_content())
    elif target_param == 'click(ctr)':
        return int(tr[0].find('./td[4]').text_content())
    elif target_param == 'movie':
        return int(tr[0].find('./td[5]').text_content())
    elif target_param == 'banner':
        return int(tr[0].find('./td[6]').text_content())
    elif target_param == 'start':
        return int(tr[0].find('./td[7]').text_content())
    elif target_param == '0sec':
        return int(tr[0].find('./td[8]').text_content())
    elif target_param == '1sec':
        return int(tr[0].find('./td[9]').text_content())
    elif target_param == 'fin':
        return int(tr[0].find('./td[10]').text_content())
    elif target_param == '25%':
        return int(tr[0].find('./td[11]').text_content())
    elif target_param == '50%':
        return int(tr[0].find('./td[12]').text_content())
    elif target_param == '75%':
        return int(tr[0].find('./td[13]').text_content())
    elif target_param == '100%':
        return int(tr[0].find('./td[14]').text_content())
