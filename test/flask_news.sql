/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50728
Source Host           : localhost:3306
Source Database       : flask_news

Target Server Type    : MYSQL
Target Server Version : 50728
File Encoding         : 65001

Date: 2019-12-01 16:21:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `news`
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `content` varchar(2000) NOT NULL,
  `types` varchar(10) NOT NULL,
  `image` varchar(300) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL,
  `view_count` int(11) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `is_valid` smallint(6) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` VALUES ('1', '朝鲜特种部队视频公布 展示士兵身体素质与意志1', '新闻内容', '推荐', '/static/img/news/01.png', null, '0', '2018-02-28 20:34:20', '1');
INSERT INTO `news` VALUES ('2', '男子长得像\"祁同伟\"挨打 打人者:为何加害检察官', '新闻内容', '百家', '/static/img/news/02.png', null, '0', '2018-03-01 20:34:29', '1');
INSERT INTO `news` VALUES ('3', '导弹来袭怎么办？日本政府呼吁国民堕入地下通道', '新闻内容', '本地', '/static/img/news/03.png', null, '0', null, '1');
INSERT INTO `news` VALUES ('4', '美监:朝在建能发射3发以上导弹的3000吨级新潜艇', '新闻内容', '推荐', '/static/img/news/04.png', null, '0', null, '1');
INSERT INTO `news` VALUES ('5', '证监会：前发审委员冯小树违法买卖股票被罚4.99亿', '新闻内容', '百家', '/static/img/news/08.png', null, '0', null, '1');
INSERT INTO `news` VALUES ('6', '外交部回应安倍参拜靖国神社:同军国主义划清界限', '新闻内容', '推荐', '/static/img/news/new1.jpg', null, '0', null, '1');
INSERT INTO `news` VALUES ('7', '\"萨德\"供地违法？韩民众联名起诉要求撤回供地', '新闻内容', '百家', '/static/img/news/new2.jpg', null, '0', null, '1');
INSERT INTO `news` VALUES ('8', '你好', '喜喜', '推荐', '/static/img/qi', null, null, '2019-11-30 22:29:52', '0');
INSERT INTO `news` VALUES ('9', '你好21', '喜喜', '推荐', '', null, null, '2019-11-30 22:29:57', '0');
