import LinkDraw

if __name__ == '__main__':
    spider = LinkDraw.LinkDraw()
    spider.set_range_page(20)
    flag = {
        "view_count": 100000,
        "collect_count": 100,
        "vote_count": 0,
        "comment_count": 10
    }
    spider.set_check_flag(flag)
    spider.run()
