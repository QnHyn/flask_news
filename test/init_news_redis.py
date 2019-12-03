#coding:utf-8

'''
初始化新闻数据
'''

from datetime import datetime

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from redis_news import RedisNews

list_news = [
    {
        "title":"朝鲜特种部队视频公布 展示士兵身体素质与意志",
        "img_url":"/static/img/news/01.png",
        "content":"在4月15日举行的朝鲜阅兵式上，除了各式展出的导弹，最亮眼的恐怕要数佩戴夜视仪的朝鲜特种部队了。4月19日，俄罗斯卫星网发布了截取自朝鲜官方电视台关于朝鲜特种部队士兵训练与展示的视频。在视频中，尽管训练科目并无太多新意，但是朝鲜士兵展示出了高度惊人的身体素质与顽强意志。",
        "is_valid": 1,
        "news_type":"推荐",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "title":"男子长得像\"祁同伟\"挨打 打人者:为何加害检察官",
        "img_url":"/static/img/news/02.png",
        "content":"因与热门电视剧中人物长相相近,男子竟然招来一顿拳打脚踢。4月19日,打人男子周某被抓获。半个月前,酒后的周某看到KTV里有一名男子很像电视剧中的反派。二话不说,周某冲上去就问你为什么要加害检察官?男子莫名其妙,回了一句神经病。周某一听气不打一处来,对着男子就是一顿拳打脚踢,嘴里面还念叨着,“叫你加害检察官,我打死你!”随后,周某趁机逃走。受伤男子立即报警,周某被上海警方上网通缉。",
        "is_valid": 1,
        "news_type":"百家",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "title":"导弹来袭怎么办？日本政府呼吁国民堕入地下通道",
        "img_url":"/static/img/news/03.JPEG",
        "content":"中新网4月21日电 据日媒报道，日本政府本月21日公布了弹道导弹可能落在国内时应采取的应对方法，呼吁民众身处室外时\“尽可能躲入坚固的建筑物或地下通道\”等",
        "is_valid": 1,
        "news_type":"本地",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "title":"美监:朝在建能发射3发以上导弹的3000吨级新潜艇",
        "img_url":"/static/img/news/04.JPEG",
        "content":"【环球网报道】据韩联社4月21日报道，美国保守媒体《华盛顿自由灯塔》20日引用联合国报告报道称，朝鲜可能对“新浦”级潜艇进行改装，使其可连发多枚潜射导弹，韩国军方负责人21日对此表示，需进一步分析，持谨慎态度",
        "is_valid": 1,
        "news_type":"推荐",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "title":"证监会：前发审委员冯小树违法买卖股票被罚4.99亿",
        "img_url":"/static/img/news/05.png",
        "content":"证监会新闻发言人张晓军21日表示，中央第七巡视组对证监会开展专项巡视期间，向证监会移交了前深交所工作人员、曾任股票发审委兼职委员冯小树涉嫌违法买卖股票的相关线索。会党委对相关线索高度重视，要求予以彻查。经过调查审理，通过对复杂商业架构的层层剖析，对繁复资金往来情况的抽丝剥茧，证监会查明，冯小树先后以岳母彭某嫦、配偶之妹何某梅名义入股拟上市公司，并在公司上市后抛售股票获利巨额利益，其交易金额累计达到2.51亿元，获利金额达2.48亿元",
        "is_valid": 1,
        "news_type":"百家",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "title":"外交部回应安倍参拜靖国神社:同军国主义划清界限",
        "img_url":"/static/img/news/06.jpg",
        "content":"新闻图片",
        "is_valid": 1,
        "news_type":"推荐",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "title":"\"萨德\"供地违法？韩民众联名起诉要求撤回供地",
        "img_url":"/static/img/news/07.jpg",
        "content":"代理本案的“民主社会律师聚会”主张，韩国《国有财产特例限制法》第4条规定，未遵守该法附表中相关法案的国有财产特例无效，该法案附表中并不包括《驻韩美军地位协定》或有关履行《驻韩美军地位协定》的特别法案，因此，韩国政府供地是违反《国有财产特例限制法》向美军提供国有财产特例。",
        "is_valid": 1,
        "news_type":"推荐",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "title":"金正恩:要由朝鲜民族自己谱写祖国统一新历史",
        "img_url":"/static/img/news/08.JPEG",
        "content":"3月5日，在朝鲜平壤，青瓦台国家安保室室长郑义溶（左）与朝鲜劳动党委员长金正恩握手。新华社平壤3月6日电 据朝中社6日报道，朝鲜最高领导人金正恩5日会见当天抵朝的韩国特使团，双方就北南首脑会晤交换意见并达成共识。报道说，金正恩在听取韩方特使转达的韩国总统文在寅有关南北首脑会晤的意愿后，与韩方交换意见并达成共识，他要求有关部门就此尽快采取相关实际举措。会见时，文在寅总统特使、青瓦台国家安保室长郑义溶向金正恩转交了文在寅的亲笔信。报道说，金正恩与韩方代表团就改善北南关系、保障朝鲜半岛和平稳定进行了开诚布公的交谈，还就缓和朝鲜半岛军事紧张状态、促进北南间多方面对话和接触、合作与交流交换了意见。金正恩说，要由朝鲜民族自己来齐心协力共同推动北南关系发展、谱写祖国统一的新历史，这是朝鲜一贯的原则立场，也是他本人坚定不移的意志。报道说，韩国特使团成员就金正恩向平昌冬奥会派遣高级别代表团等多个大规模代表团、帮助大会取得圆满成功表示感谢。金正恩说，作为血脉相连的同一民族，共同庆祝民族喜事并互相帮助，这次冬奥会是营造北南和解团结与对话良好气氛的重要契机。除郑义溶外，特使团其他成员韩国国家情报院院长徐薰、统一部次官千海成、国家情报院次长金相均和青瓦台国政状况室室长尹建永也参加了会见。朝鲜劳动党中央委员会副委员长金英哲和朝鲜劳动党中央委员会第一副部长金与正会见时在座。据朝中社报道，金正恩5日为韩国特使团成员举行了晚宴，金正恩的夫人李雪主，以及金英哲、金与正等参加晚宴。另据韩国媒体报道，韩国总统府青瓦台发言人金宜谦6日说，5日的会见和晚宴持续4个多小时。特使团将在结束后续会谈后，于6日下午返回首尔。青瓦台消息人士表示，这次会见成果“不令人失望”，韩朝就包括首脑会晤等事项达成一定程度的一致。",
        "is_valid": 1,
        "news_type":"百家",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
]


def main():
    redis_news = RedisNews()
    rest = redis_news.init_news(list_news)

if __name__ == "__main__":
    main()