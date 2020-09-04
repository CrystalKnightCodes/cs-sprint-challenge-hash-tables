
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_cache = {}
    route = []
    places = 0
    current_place = 'NONE'

    for ticket in tickets:
        ticket_cache[ticket.source] = ticket.destination

    while places < length:
        next_place = ticket_cache[current_place]
        route.append(next_place)

        current_place = next_place
        places += 1

    return route
