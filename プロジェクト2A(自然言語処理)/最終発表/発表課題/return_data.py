import urllib
import untangle
import urllib.parse

if __name__ == '__main__':
    start='1'#発言の通し番号
    while start!=None:
        keyword = '安倍晋三'
        startdate='2020-01-01'
        enddate= '2020-06-01'
        meeting='予算委員会'
        url = 'http://kokkai.ndl.go.jp/api/1.0/speech?'+urllib.parse.quote('startRecord='+ start
        + '&maximumRecords=100&speaker='+ keyword
        + '&nameOfMeeting='+ meeting
        + '&from=' + startdate
        + '&until='+ enddate)
        #Get信号のリクエストの検索結果（XML）
        obj = untangle.parse(url)

        for record in obj.data.records.record:
            speechrecord = record.recordData.speechRecord
            print(speechrecord.date.cdata,
                speechrecord.speech.cdata)

            file=open('2020.txt','a')
            file.write(speechrecord.speech.cdata)
            file.close()
            #一度に１００件しか帰ってこないので、開始位置を変更して繰り返しGET関数を送信
        start=obj.data.nextRecordPosition.cdata