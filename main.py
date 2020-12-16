import LinkDraw

if __name__ == '__main__':
    spider = LinkDraw.LinkDraw()
    spider.set_range_page(50)
    flag = {
        "view_count": 30000,
        "collect_count": 100,
        "vote_count": 50,
        "comment_count": 10
    }
    spider.set_check_flag(flag)
    spider.run()
