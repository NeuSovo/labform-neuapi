from lxml import etree

s = '''
<html >
         <head>
        <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>资源授权</title>
    <!-- zui -->
        <script type="text/javascript" src="/odc/plugins/bootstrap/js/jquery.min.js"></script>
        <script type="text/javascript" src="/odc/plugins/bootstrap/js/bootstrap.min.js"></script>
    <link href="/odc/plugins/zui-1.6.0/css/zui.min.css" rel="stylesheet">
        </head>
        <body>

<h2>应用:实验室预约管理系统</h2>
<div class="example">
<div class="alert alert-primary with-icon">
    <i class="icon-info-sign"></i>
    <div class="content">
      <h4>雷洋林[学生]</strong>,您好:</h4>
      <hr>
      <p>应用:<strong>《实验室预约管理系统》</strong>,申请获取您的信息，请仔细确认。</p>
    </div>
  </div>
</div>
<form id="loginfm" method="post" action="/odc/api/auth/user/v1/authconfirm.do">
<input type="hidden" name="consid" value="LMS">
<input type="hidden" name="userid" value="16180601031">
<input type="hidden" name="timestamp" value="1560831200">
<input type="hidden" name="rand" value="414310">
<input type="hidden" name="callback" value="http://127.0.0.1:5000/user/callback">
<input type="hidden" name="sign" value="9ac00656b11642a4c304112bdb9cd92e">
<div class="panel">
    <div class="panel-heading">本人确认应用资源授权列表</div>
    <ul class="list-group">

    <li class="list-group-item"><input disabled type="checkbox" checked>申请用户授权登录</li>

    <li class="list-group-item"><input disabled type="checkbox" checked>用户授权登录</li>

    <li class="list-group-item"><input disabled type="checkbox" checked>获取用户基本信息（姓名、系所信息）</li>

    </ul>
</div>
'''

se = etree.HTML(s)
# print (se.xpath('//div[@class="example"]/div/div/h4/text()'))
action = se.xpath('//form[@id="loginfm"]/@action')

sign = se.xpath('//form[@id="loginfm"]/input[@name="sign"]/@value')

print (action, sign)