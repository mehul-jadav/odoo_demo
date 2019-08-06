from odoo import http

class Openacademy(http.Controller):
    @http.route('/home', auth='public')
    def index(self, **kw):
        return "<h3> <marquee> Get a ride in minutes. </marquee> </h3> " \
               "<p> <h4> <marquee direction='right'> Or become a driver and earn money on your schedule.</h4> </marquee>  <br>" \
               "</p> <center> Uber is finding you better ways to move, work, and succeed. </center>"


