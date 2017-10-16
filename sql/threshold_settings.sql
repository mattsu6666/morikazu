CREATE TABLE IF NOT EXISTS `threshold_settings` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `campaign_id` INT UNSIGNED NOT NULL,
  `ad_id` INT UNSIGNED NOT NULL,
  `target_param` ENUM('imp', 'click(ctr)', 'movie',	'banner', 'start', '0sec', '1sec', 'fin', '25%', '50%', '75%', '100%') NOT NULL DEFAULT 'imp',
  `threshold` INT UNSIGNED NOT NULL,
  `status` ENUM('active', 'inactive') NOT NULL DEFAULT 'active',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  CHARSET=utf8;