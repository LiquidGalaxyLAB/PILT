from races.models import Participant, RaceParticipant,Position


def create_routeparticipant_kml(positions,raceparticipant):
    filename = "liquidgalaxy/kml/" + raceparticipant.participant.user.username + ".kml"
    auxImagePath = raceparticipant.participant.image.split("&")
    imagePath = auxImagePath[0] + "&amp;" + auxImagePath[1]

    with open(filename, "w") as kml_file:
        kml_file.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
            "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n" +
            "\t<Document>\n" +
            "\t\t<Style id=\"" + raceparticipant.participant.user.username + "\">\n" +
            "\t\t\t<IconStyle>\n" +
            "\t\t\t\t<scale>2.0</scale>\n" +
            "\t\t\t\t<Icon>\n" +
            "\t\t\t\t\t<href>" + imagePath + "</href>\n" +
            "\t\t\t\t</Icon>\n" +
            "\t\t\t</IconStyle>\n" +
            "\t\t</Style>\n" +
            "\t\t<Style id=\"thickBlackLine\">\n" +
            "\t\t\t<LineStyle>\n"+
            "\t\t\t\t<color>ff000000</color>\n" +
            "\t\t\t\t<width>20</width>\n" +
            "\t\t\t</LineStyle>\n" +
            "\t\t</Style>\n" +
            "\t\t<Placemark>\n" +
            "\t\t\t<styleUrl>#thickBlackLine</styleUrl>\n" +
            "\t\t\t<LineString>\n" +
            "\t\t\t\t<tessellate>1</tessellate>\n" +
            "\t\t\t\t<coordinates>\n")
        for position in positions:
            kml_file.write("\t\t\t\t" + str(position.longitude) +","+ str(position.latitude)+","+str(position.height)+ "\n")
        kml_file.write("\t\t\t\t</coordinates>\n" +
            "\t\t\t</LineString>\n" +
           "\t\t</Placemark>\n" +
            "\t\t<Placemark>\n" +
            "\t\t\t<name>" + raceparticipant.participant.user.username + "</name>\n" +
            "\t\t\t<description>The participant"+ raceparticipant.participant.user.username +"</description>\n" +
            "\t\t\t<styleUrl>#"+raceparticipant.participant.user.username+"</styleUrl>\n" +
            "\t\t\t<Point>\n" +
            "\t\t\t\t<extrude>1</extrude>\n" +
            "\t\t\t\t<altitudeMode>relativeToGround</altitudeMode>\n" +
            "\t\t\t\t<coordinates>" +
            str(position.longitude) + "," + str(position.latitude) + "," +str(position.height) +
            "</coordinates>\n" +
            "\t\t\t</Point>\n" +
            "\t\t</Placemark>\n" +
            "\t</Document>\n" +
            "</kml>")
        kml_file.close()
        print("hola")





def create_participant_kml(positions,raceparticipant):
    filename="liquidgalaxy/kml/"+raceparticipant.participant.user.username+".kml"
    positions=list(positions)
    position=positions[-1]
    auxImagePath= raceparticipant.participant.image.split("&")
    imagePath=auxImagePath[0]+"&amp;"+auxImagePath[1]
    with open(filename, "w") as kml_file:
        kml_file.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
            "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n" +
            "\t<Document>\n" +
            "\t\t<Style id=\""+raceparticipant.participant.user.username+"\">\n" +
            "\t\t\t<IconStyle>\n" +
            "\t\t\t\t<scale>2.0</scale>\n" +
            "\t\t\t\t<Icon>\n" +
            "\t\t\t\t\t<href>" + imagePath + "</href>\n" +
            "\t\t\t\t</Icon>\n" +
            "\t\t\t</IconStyle>\n" +
            "\t\t</Style>\n" +
            "\t\t<Placemark>\n" +
            "\t\t\t<name>" + raceparticipant.participant.user.username + "</name>\n" +
            "\t\t\t<description>The participant"+ raceparticipant.participant.user.username +"</description>\n" +
            "\t\t\t<styleUrl>#"+raceparticipant.participant.user.username+"</styleUrl>\n" +
            "\t\t\t<Point>\n" +
            "\t\t\t\t<extrude>1</extrude>\n" +
            "\t\t\t\t<altitudeMode>relativeToGround</altitudeMode>\n" +
            "\t\t\t\t<coordinates>" +
            str(position.longitude) + "," + str(position.latitude) + "," +
            str(position.height) +
            "</coordinates>\n" +
            "\t\t\t</Point>\n" +
            "\t\t</Placemark>\n" +
            "\t</Document>\n" +
            "</kml>")
        kml_file.close()
        print("hola")