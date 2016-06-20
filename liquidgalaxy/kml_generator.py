from races.models import Participant, RaceParticipant,Position


def placemark_kml(participant,raceparticipant):
    participant = Participant.objects.get(participant=participant)
    position = RaceParticipant.objects.all(raceparticipant=raceparticipant)
    filename=participant.username+".kml"
    with open(filename, "w") as kml_file:
        kml_file.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
            "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n" +
            "\t<Document>\n" +
            "\t\t<Style id=\"drone\">\n" +
            "\t\t\t<IconStyle>\n" +
            "\t\t\t\t<Icon>\n" +
            "\t\t\t\t\t<href>" + participant.image + "</href>\n" +
            "\t\t\t\t\t<scale>1.0</scale>\n" +
            "\t\t\t\t</Icon>\n" +
            "\t\t\t</IconStyle>\n" +
            "\t\t</Style>\n" +
            "\t\t<Placemark>\n" +
            "\t\t\t<name>" + participant.user.username + "</name>\n" +
            "\t\t\t<description>The participant"+ participant.user.username +"</description>\n" +
            "\t\t\t<styleUrl>#drone</styleUrl>\n" +
            "\t\t\t<Point>\n" +
            "\t\t\t\t<altitudeMode>relativeToGround</altitudeMode>\n" +
            "\t\t\t\t<coordinates>" +
            str(position.longitude) + "," + str(position.latitude) + "," +
            str(position.height) +
            "</coordinates>\n" +
            "\t\t\t</Point>\n" +
            "\t\t</Placemark>\n" +
            "\t</Document>\n" +
            "</kml>")