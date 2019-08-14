# coding=utf-8


# 将来变量尽量上抬到xlsm
# -------------------------------------ENVIRON BELOW--------------------------------------------------
# 公共gateway入口
API = 'api/gateway.do?method='
# 菲律宾DEV环境
PH_DEV_ENVIRON = 'http://lps-web.ph-dev.hidataverse.com/' + API
# 泰国UAT环境
TH_UAT_ENVIRON = 'https://lps-web.th-uat.hidataverse.com/' + API
# 菲律宾SIT环境（原TH_TEST环境）
PH_SIT_ENVIRON = 'https://lps-web.ph-sit.hidataverse.com/' + API

environs = {'PH_DEV': PH_DEV_ENVIRON, 'TH_UAT': TH_UAT_ENVIRON, 'PH_SIT': PH_SIT_ENVIRON}


def getEnviron(env):
    return environs[env]


def getMethod(env):
    return methodMap[env]


# -------------------------------------REST URL BELOW--------------------------------------------------

# 登录前预校验
PREQUERY = "qihoo.sdk.user.mobile.prequery"
# 消息中心消息数
MCMSG_COUNTNEW = "qihoo.sdk.inform.mcmsg.countnew"
# 消息中心列表查询
MCMSG_QUERY = "qihoo.sdk.inform.mcmsg.query"
# WEB发送验证码短信
SMS_SEND = "qihoo.sdk.inform.sms.send"
# 首页信息查询
APPL_SUMMARY_QUERY = "qihoo.sdk.appl.summary.query"

# 注册
REGISTER = "qihoo.sdk.user.register"
# 登录
LOGIN = "qihoo.sdk.user.mobile.login"
# 授信
ITEM_COMMIT = "qihoo.sdk.appl.item.commit"

# 还款记录查询
REFUND_RECORD_QUERY = "qihoo.sdk.appl.refund.record.query"
# 查询补件信息
SUPPLEMENT_LIST_QUERY = "qihoo.sdk.appl.supplementlist.query"

methodMap = {'login': LOGIN, 'register': REGISTER, "summaryQuery": APPL_SUMMARY_QUERY, "itemCommit": ITEM_COMMIT}
