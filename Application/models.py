from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import TextField, IntegerField, CharField, DateField
from django.db import models
from django.db.models.signals import post_save
from Hostel_office.models import Department

from django.dispatch import receiver
import os

import login.models as login_models

from datetime import datetime
from django.utils import timezone

state_choices = ((None, 'State'),
                 ("Andhra Pradesh", "Andhra Pradesh"),
                 ("Arunachal Pradesh", "Arunachal Pradesh"),
                 ("Assam", "Assam"),
                 ("Bihar", "Bihar"),
                 ("Chandigarh (UT)", "Chandigarh (UT)"),
                 ("Chhattisgarh", "Chhattisgarh"),
                 ("Dadra and Nagar Haveli (UT)", "Dadra and Nagar Haveli (UT)"),
                 ("Daman and Diu (UT)", "Daman and Diu (UT)"),
                 ("Delhi (NCT)", "Delhi (NCT)"),
                 ("Goa", "Goa"),
                 ("Gujarat", "Gujarat"),
                 ("Haryana", "Haryana"),
                 ('Himachal Pradesh', 'Himachal Pradesh'),
                 ("Jammu and Kashmir", "Jammu and Kashmir"),
                 ("Jharkhand", "Jharkhand"),
                 ("Karnataka", "Karnataka"),
                 ("Kerala", "Kerala"),
                 ("Lakshadweep (UT)", "Lakshadweep (UT)"),
                 ("Madhya Pradesh", "Madhya Pradesh"),
                 ("Maharashtra", "Maharashtra"),
                 ("Manipur", "Manipur"),
                 ("Meghalaya", "Meghalaya"),
                 ("Mizoram", "Mizoram"),
                 ("Nagaland", "Nagaland"),
                 ("Odisha", "Odisha"),
                 ("Puducherry (UT)", "Puducherry (UT)"),
                 ("Punjab", "Punjab"),
                 ("Rajasthan", "Rajasthan"),
                 ("Sikkim", "Sikkim"),
                 ("Tamil Nadu", "Tamil Nadu"),
                 ("Telangana", "Telangana"),
                 ("Tripura", "Tripura"),
                 ("Uttarakhand", "Uttarakhand"),
                 ("Uttar Pradesh", "Uttar Pradesh"),
                 ("West Bengal", "West Bengal"))

district_choices = [(None, 'District'), ('Anantapur', 'Anantapur'), ('Chittoor', 'Chittoor'),
                    ('East Godavari', 'East Godavari'),
                    ('Guntur', 'Guntur'),
                    ('Krishna', 'Krishna'), ('Kurnool', 'Kurnool'), ('Nellore', 'Nellore'), ('Prakasam', 'Prakasam'),
                    ('Srikakulam', 'Srikakulam'), ('Visakhapatnam', 'Visakhapatnam'), ('Vizianagaram', 'Vizianagaram'),
                    ('West Godavari', 'West Godavari'), ('YSR Kadapa', 'YSR Kadapa'), ('Tawang', 'Tawang'),
                    ('West Kameng', 'West Kameng'), ('East Kameng', 'East Kameng'), ('Papum Pare', 'Papum Pare'),
                    ('Kurung Kumey', 'Kurung Kumey'), ('Kra Daadi', 'Kra Daadi'),
                    ('Lower Subansiri', 'Lower Subansiri'),
                    ('Upper Subansiri', 'Upper Subansiri'), ('West Siang', 'West Siang'), ('East Siang', 'East Siang'),
                    ('Siang', 'Siang'), ('Upper Siang', 'Upper Siang'), ('Lower Siang', 'Lower Siang'),
                    ('Lower Dibang Valley', 'Lower Dibang Valley'), ('Dibang Valley', 'Dibang Valley'),
                    ('Anjaw', 'Anjaw'),
                    ('Lohit', 'Lohit'), ('Namsai', 'Namsai'), ('Changlang', 'Changlang'), ('Tirap', 'Tirap'),
                    ('Longding', 'Longding'),
                    ('Baksa', 'Baksa'), ('Barpeta', 'Barpeta'), ('Biswanath', 'Biswanath'),
                    ('Bongaigaon', 'Bongaigaon'),
                    ('Cachar', 'Cachar'), ('Charaideo', 'Charaideo'), ('Chirang', 'Chirang'), ('Darrang', 'Darrang'),
                    ('Dhemaji', 'Dhemaji'), ('Dhubri', 'Dhubri'), ('Dibrugarh', 'Dibrugarh'), ('Goalpara', 'Goalpara'),
                    ('Golaghat', 'Golaghat'), ('Hailakandi', 'Hailakandi'), ('Hojai', 'Hojai'), ('Jorhat', 'Jorhat'),
                    ('Kamrup Metropolitan', 'Kamrup Metropolitan'), ('Kamrup', 'Kamrup'),
                    ('Karbi Anglong', 'Karbi Anglong'),
                    ('Karimganj', 'Karimganj'), ('Kokrajhar', 'Kokrajhar'), ('Lakhimpur', 'Lakhimpur'),
                    ('Majuli', 'Majuli'),
                    ('Morigaon', 'Morigaon'), ('Nagaon', 'Nagaon'), ('Nalbari', 'Nalbari'),
                    ('Dima Hasao', 'Dima Hasao'),
                    ('Sivasagar', 'Sivasagar'), ('Sonitpur', 'Sonitpur'),
                    ('South Salmara-Mankachar', 'South Salmara-Mankachar'),
                    ('Tinsukia', 'Tinsukia'), ('Udalguri', 'Udalguri'), ('West Karbi Anglong', 'West Karbi Anglong'),
                    ('Araria', 'Araria'), ('Arwal', 'Arwal'), ('Aurangabad', 'Aurangabad'), ('Banka', 'Banka'),
                    ('Begusarai', 'Begusarai'), ('Bhagalpur', 'Bhagalpur'), ('Bhojpur', 'Bhojpur'), ('Buxar', 'Buxar'),
                    ('Darbhanga', 'Darbhanga'), ('East Champaran (Motihari)', 'East Champaran (Motihari)'),
                    ('Gaya', 'Gaya'),
                    ('Gopalganj', 'Gopalganj'), ('Jamui', 'Jamui'), ('Jehanabad', 'Jehanabad'),
                    ('Kaimur (Bhabua)', 'Kaimur (Bhabua)'),
                    ('Katihar', 'Katihar'), ('Khagaria', 'Khagaria'), ('Kishanganj', 'Kishanganj'),
                    ('Lakhisarai', 'Lakhisarai'),
                    ('Madhepura', 'Madhepura'), ('Madhubani', 'Madhubani'), ('Munger (Monghyr)', 'Munger (Monghyr)'),
                    ('Muzaffarpur', 'Muzaffarpur'), ('Nalanda', 'Nalanda'), ('Nawada', 'Nawada'), ('Patna', 'Patna'),
                    ('Purnia (Purnea)', 'Purnia (Purnea)'), ('Rohtas', 'Rohtas'), ('Saharsa', 'Saharsa'),
                    ('Samastipur', 'Samastipur'),
                    ('Saran', 'Saran'), ('Sheikhpura', 'Sheikhpura'), ('Sheohar', 'Sheohar'),
                    ('Sitamarhi', 'Sitamarhi'),
                    ('Siwan', 'Siwan'), ('Supaul', 'Supaul'), ('Vaishali', 'Vaishali'),
                    ('West Champaran', 'West Champaran'),
                    ('Chandigarh', 'Chandigarh'), ('Balod', 'Balod'), ('Baloda Bazar', 'Baloda Bazar'),
                    ('Balrampur', 'Balrampur'),
                    ('Bastar', 'Bastar'), ('Bemetara', 'Bemetara'), ('Bijapur', 'Bijapur'), ('Bilaspur', 'Bilaspur'),
                    ('Dantewada (South Bastar)', 'Dantewada (South Bastar)'), ('Dhamtari', 'Dhamtari'),
                    ('Durg', 'Durg'),
                    ('Gariyaband', 'Gariyaband'), ('Janjgir-Champa', 'Janjgir-Champa'), ('Jashpur', 'Jashpur'),
                    ('Kabirdham (Kawardha)', 'Kabirdham (Kawardha)'),
                    ('Kanker (North Bastar)', 'Kanker (North Bastar)'),
                    ('Kondagaon', 'Kondagaon'), ('Korba', 'Korba'), ('Korea (Koriya)', 'Korea (Koriya)'),
                    ('Mahasamund', 'Mahasamund'),
                    ('Mungeli', 'Mungeli'), ('Narayanpur', 'Narayanpur'), ('Raigarh', 'Raigarh'), ('Raipur', 'Raipur'),
                    ('Rajnandgaon', 'Rajnandgaon'), ('Sukma', 'Sukma'), ('Surajpur  ', 'Surajpur  '),
                    ('Surguja', 'Surguja'),
                    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman', 'Daman'), ('Diu', 'Diu'),
                    ('Central Delhi', 'Central Delhi'), ('East Delhi', 'East Delhi'), ('New Delhi', 'New Delhi'),
                    ('North Delhi', 'North Delhi'), ('North East  Delhi', 'North East  Delhi'),
                    ('North West  Delhi', 'North West  Delhi'), ('Shahdara', 'Shahdara'),
                    ('South Delhi', 'South Delhi'),
                    ('South East Delhi', 'South East Delhi'), ('South West  Delhi', 'South West  Delhi'),
                    ('West Delhi', 'West Delhi'),
                    ('North Goa', 'North Goa'), ('South Goa', 'South Goa'), ('Ahmedabad', 'Ahmedabad'),
                    ('Amreli', 'Amreli'),
                    ('Anand', 'Anand'), ('Aravalli', 'Aravalli'), ('Banaskantha (Palanpur)', 'Banaskantha (Palanpur)'),
                    ('Bharuch', 'Bharuch'), ('Bhavnagar', 'Bhavnagar'), ('Botad', 'Botad'),
                    ('Chhota Udepur', 'Chhota Udepur'),
                    ('Dahod', 'Dahod'), ('Dangs (Ahwa)', 'Dangs (Ahwa)'), ('Devbhoomi Dwarka', 'Devbhoomi Dwarka'),
                    ('Gandhinagar', 'Gandhinagar'), ('Gir Somnath', 'Gir Somnath'), ('Jamnagar', 'Jamnagar'),
                    ('Junagadh', 'Junagadh'),
                    ('Kachchh', 'Kachchh'), ('Kheda (Nadiad)', 'Kheda (Nadiad)'), ('Mahisagar', 'Mahisagar'),
                    ('Mehsana', 'Mehsana'),
                    ('Morbi', 'Morbi'), ('Narmada (Rajpipla)', 'Narmada (Rajpipla)'), ('Navsari', 'Navsari'),
                    ('Panchmahal (Godhra)', 'Panchmahal (Godhra)'), ('Patan', 'Patan'), ('Porbandar', 'Porbandar'),
                    ('Rajkot', 'Rajkot'), ('Sabarkantha (Himmatnagar)', 'Sabarkantha (Himmatnagar)'),
                    ('Surat', 'Surat'),
                    ('Surendranagar', 'Surendranagar'), ('Tapi (Vyara)', 'Tapi (Vyara)'), ('Vadodara', 'Vadodara'),
                    ('Valsad', 'Valsad'), ('Ambala', 'Ambala'), ('Bhiwani', 'Bhiwani'),
                    ('Charkhi Dadri', 'Charkhi Dadri'),
                    ('Faridabad', 'Faridabad'), ('Fatehabad', 'Fatehabad'), ('Gurgaon', 'Gurgaon'), ('Hisar', 'Hisar'),
                    ('Jhajjar', 'Jhajjar'), ('Jind', 'Jind'), ('Kaithal', 'Kaithal'), ('Karnal', 'Karnal'),
                    ('Kurukshetra', 'Kurukshetra'), ('Mahendragarh', 'Mahendragarh'), ('Mewat', 'Mewat'),
                    ('Palwal', 'Palwal'),
                    ('Panchkula', 'Panchkula'), ('Panipat', 'Panipat'), ('Rewari', 'Rewari'), ('Rohtak', 'Rohtak'),
                    ('Sirsa', 'Sirsa'),
                    ('Sonipat', 'Sonipat'), ('Yamunanagar', 'Yamunanagar'), ('Bilaspur', 'Bilaspur'),
                    ('Chamba', 'Chamba'),
                    ('Hamirpur', 'Hamirpur'), ('Kangra', 'Kangra'), ('Kinnaur', 'Kinnaur'), ('Kullu', 'Kullu'),
                    ('Lahaul &amp; Spiti', 'Lahaul &amp; Spiti'), ('Mandi', 'Mandi'), ('Shimla', 'Shimla'),
                    ('Sirmaur (Sirmour)', 'Sirmaur (Sirmour)'), ('Solan', 'Solan'), ('Una', 'Una'),
                    ('Anantnag', 'Anantnag'),
                    ('Bandipore', 'Bandipore'), ('Baramulla', 'Baramulla'), ('Budgam', 'Budgam'), ('Doda', 'Doda'),
                    ('Ganderbal', 'Ganderbal'), ('Jammu', 'Jammu'), ('Kargil', 'Kargil'), ('Kathua', 'Kathua'),
                    ('Kishtwar', 'Kishtwar'), ('Kulgam', 'Kulgam'), ('Kupwara', 'Kupwara'), ('Leh', 'Leh'),
                    ('Poonch', 'Poonch'),
                    ('Pulwama', 'Pulwama'), ('Rajouri', 'Rajouri'), ('Ramban', 'Ramban'), ('Reasi', 'Reasi'),
                    ('Samba', 'Samba'),
                    ('Shopian', 'Shopian'), ('Srinagar', 'Srinagar'), ('Udhampur', 'Udhampur'), ('Bokaro', 'Bokaro'),
                    ('Chatra', 'Chatra'), ('Deoghar', 'Deoghar'), ('Dhanbad', 'Dhanbad'), ('Dumka', 'Dumka'),
                    ('East Singhbhum', 'East Singhbhum'), ('Garhwa', 'Garhwa'), ('Giridih', 'Giridih'),
                    ('Godda', 'Godda'),
                    ('Gumla', 'Gumla'), ('Hazaribag', 'Hazaribag'), ('Jamtara', 'Jamtara'), ('Khunti', 'Khunti'),
                    ('Koderma', 'Koderma'), ('Latehar', 'Latehar'), ('Lohardaga', 'Lohardaga'), ('Pakur', 'Pakur'),
                    ('Palamu', 'Palamu'), ('Ramgarh', 'Ramgarh'), ('Ranchi', 'Ranchi'), ('Sahibganj', 'Sahibganj'),
                    ('Seraikela-Kharsawan', 'Seraikela-Kharsawan'), ('Simdega', 'Simdega'),
                    ('West Singhbhum', 'West Singhbhum'),
                    ('Bagalkot', 'Bagalkot'), ('Ballari (Bellary)', 'Ballari (Bellary)'),
                    ('Belagavi (Belgaum)', 'Belagavi (Belgaum)'),
                    ('Bengaluru (Bangalore) Rural', 'Bengaluru (Bangalore) Rural'),
                    ('Bengaluru (Bangalore) Urban', 'Bengaluru (Bangalore) Urban'), ('Bidar', 'Bidar'),
                    ('Chamarajanagar', 'Chamarajanagar'), ('Chikballapur', 'Chikballapur'),
                    ('Chikkamagaluru (Chikmagalur)', 'Chikkamagaluru (Chikmagalur)'), ('Chitradurga', 'Chitradurga'),
                    ('Dakshina Kannada', 'Dakshina Kannada'), ('Davangere', 'Davangere'), ('Dharwad', 'Dharwad'),
                    ('Gadag', 'Gadag'),
                    ('Hassan', 'Hassan'), ('Haveri', 'Haveri'), ('Kalaburagi (Gulbarga)', 'Kalaburagi (Gulbarga)'),
                    ('Kodagu', 'Kodagu'), ('Kolar', 'Kolar'), ('Koppal', 'Koppal'), ('Mandya', 'Mandya'),
                    ('Mysuru (Mysore)', 'Mysuru (Mysore)'), ('Raichur', 'Raichur'), ('Ramanagara', 'Ramanagara'),
                    ('Shivamogga (Shimoga)', 'Shivamogga (Shimoga)'), ('Tumakuru (Tumkur)', 'Tumakuru (Tumkur)'),
                    ('Udupi', 'Udupi'),
                    ('Uttara Kannada (Karwar)', 'Uttara Kannada (Karwar)'),
                    ('Vijayapura (Bijapur)', 'Vijayapura (Bijapur)'),
                    ('Yadgir', 'Yadgir'), ('Alappuzha', 'Alappuzha'), ('Ernakulam', 'Ernakulam'), ('Idukki', 'Idukki'),
                    ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod'), ('Kollam', 'Kollam'), ('Kottayam', 'Kottayam'),
                    ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Palakkad', 'Palakkad'),
                    ('Pathanamthitta', 'Pathanamthitta'), ('Thiruvananthapuram', 'Thiruvananthapuram'),
                    ('Thrissur', 'Thrissur'),
                    ('Wayanad', 'Wayanad'), ('Agatti', 'Agatti'), ('Amini', 'Amini'), ('Androth', 'Androth'),
                    ('Bithra', 'Bithra'),
                    ('Chethlath', 'Chethlath'), ('Kavaratti', 'Kavaratti'), ('Kadmath', 'Kadmath'),
                    ('Kalpeni', 'Kalpeni'),
                    ('Kilthan', 'Kilthan'), ('Minicoy', 'Minicoy'), ('Agar Malwa', 'Agar Malwa'),
                    ('Alirajpur', 'Alirajpur'),
                    ('Anuppur', 'Anuppur'), ('Ashoknagar', 'Ashoknagar'), ('Balaghat', 'Balaghat'),
                    ('Barwani', 'Barwani'),
                    ('Betul', 'Betul'), ('Bhind', 'Bhind'), ('Bhopal', 'Bhopal'), ('Burhanpur', 'Burhanpur'),
                    ('Chhatarpur', 'Chhatarpur'), ('Chhindwara', 'Chhindwara'), ('Damoh', 'Damoh'), ('Datia', 'Datia'),
                    ('Dewas', 'Dewas'), ('Dhar', 'Dhar'), ('Dindori', 'Dindori'), ('Guna', 'Guna'),
                    ('Gwalior', 'Gwalior'),
                    ('Harda', 'Harda'), ('Hoshangabad', 'Hoshangabad'), ('Indore', 'Indore'), ('Jabalpur', 'Jabalpur'),
                    ('Jhabua', 'Jhabua'), ('Katni', 'Katni'), ('Khandwa', 'Khandwa'), ('Khargone', 'Khargone'),
                    ('Mandla', 'Mandla'),
                    ('Mandsaur', 'Mandsaur'), ('Morena', 'Morena'), ('Narsinghpur', 'Narsinghpur'),
                    ('Neemuch', 'Neemuch'),
                    ('Panna', 'Panna'), ('Raisen', 'Raisen'), ('Rajgarh', 'Rajgarh'), ('Ratlam', 'Ratlam'),
                    ('Rewa', 'Rewa'),
                    ('Sagar', 'Sagar'), ('Satna', 'Satna'), ('Sehore', 'Sehore'), ('Seoni', 'Seoni'),
                    ('Shahdol', 'Shahdol'),
                    ('Shajapur', 'Shajapur'), ('Sheopur', 'Sheopur'), ('Shivpuri', 'Shivpuri'), ('Sidhi', 'Sidhi'),
                    ('Singrauli', 'Singrauli'), ('Tikamgarh', 'Tikamgarh'), ('Ujjain', 'Ujjain'), ('Umaria', 'Umaria'),
                    ('Vidisha', 'Vidisha'), ('Ahmednagar', 'Ahmednagar'), ('Akola', 'Akola'), ('Amravati', 'Amravati'),
                    ('Aurangabad', 'Aurangabad'), ('Beed', 'Beed'), ('Bhandara', 'Bhandara'), ('Buldhana', 'Buldhana'),
                    ('Chandrapur', 'Chandrapur'), ('Dhule', 'Dhule'), ('Gadchiroli', 'Gadchiroli'),
                    ('Gondia', 'Gondia'),
                    ('Hingoli', 'Hingoli'), ('Jalgaon', 'Jalgaon'), ('Jalna', 'Jalna'), ('Kolhapur', 'Kolhapur'),
                    ('Latur', 'Latur'),
                    ('Mumbai City', 'Mumbai City'), ('Mumbai Suburban', 'Mumbai Suburban'), ('Nagpur', 'Nagpur'),
                    ('Nanded', 'Nanded'),
                    ('Nandurbar', 'Nandurbar'), ('Nashik', 'Nashik'), ('Osmanabad', 'Osmanabad'),
                    ('Palghar', 'Palghar'),
                    ('Parbhani', 'Parbhani'), ('Pune', 'Pune'), ('Raigad', 'Raigad'), ('Ratnagiri', 'Ratnagiri'),
                    ('Sangli', 'Sangli'),
                    ('Satara', 'Satara'), ('Sindhudurg', 'Sindhudurg'), ('Solapur', 'Solapur'), ('Thane', 'Thane'),
                    ('Wardha', 'Wardha'), ('Washim', 'Washim'), ('Yavatmal', 'Yavatmal'), ('Bishnupur', 'Bishnupur'),
                    ('Chandel', 'Chandel'), ('Churachandpur', 'Churachandpur'), ('Imphal East', 'Imphal East'),
                    ('Imphal West', 'Imphal West'), ('Jiribam', 'Jiribam'), ('Kakching', 'Kakching'),
                    ('Kamjong', 'Kamjong'),
                    ('Kangpokpi', 'Kangpokpi'), ('Noney', 'Noney'), ('Pherzawl', 'Pherzawl'), ('Senapati', 'Senapati'),
                    ('Tamenglong', 'Tamenglong'), ('Tengnoupal', 'Tengnoupal'), ('Thoubal', 'Thoubal'),
                    ('Ukhrul', 'Ukhrul'),
                    ('East Garo Hills', 'East Garo Hills'), ('East Jaintia Hills', 'East Jaintia Hills'),
                    ('East Khasi Hills', 'East Khasi Hills'), ('North Garo Hills', 'North Garo Hills'),
                    ('Ri Bhoi', 'Ri Bhoi'),
                    ('South Garo Hills', 'South Garo Hills'), ('South West Garo Hills ', 'South West Garo Hills '),
                    ('South West Khasi Hills', 'South West Khasi Hills'), ('West Garo Hills', 'West Garo Hills'),
                    ('West Jaintia Hills', 'West Jaintia Hills'), ('West Khasi Hills', 'West Khasi Hills'),
                    ('Aizawl', 'Aizawl'),
                    ('Champhai', 'Champhai'), ('Kolasib', 'Kolasib'), ('Lawngtlai', 'Lawngtlai'),
                    ('Lunglei', 'Lunglei'),
                    ('Mamit', 'Mamit'), ('Saiha', 'Saiha'), ('Serchhip', 'Serchhip'), ('Dimapur', 'Dimapur'),
                    ('Kiphire', 'Kiphire'),
                    ('Kohima', 'Kohima'), ('Longleng', 'Longleng'), ('Mokokchung', 'Mokokchung'), ('Mon', 'Mon'),
                    ('Peren', 'Peren'),
                    ('Phek', 'Phek'), ('Tuensang', 'Tuensang'), ('Wokha', 'Wokha'), ('Zunheboto', 'Zunheboto'),
                    ('Angul', 'Angul'),
                    ('Balangir', 'Balangir'), ('Balasore', 'Balasore'), ('Bargarh', 'Bargarh'), ('Bhadrak', 'Bhadrak'),
                    ('Boudh', 'Boudh'), ('Cuttack', 'Cuttack'), ('Deogarh', 'Deogarh'), ('Dhenkanal', 'Dhenkanal'),
                    ('Gajapati', 'Gajapati'), ('Ganjam', 'Ganjam'), ('Jagatsinghapur', 'Jagatsinghapur'),
                    ('Jajpur', 'Jajpur'),
                    ('Jharsuguda', 'Jharsuguda'), ('Kalahandi', 'Kalahandi'), ('Kandhamal', 'Kandhamal'),
                    ('Kendrapara', 'Kendrapara'),
                    ('Kendujhar (Keonjhar)', 'Kendujhar (Keonjhar)'), ('Khordha', 'Khordha'), ('Koraput', 'Koraput'),
                    ('Malkangiri', 'Malkangiri'), ('Mayurbhanj', 'Mayurbhanj'), ('Nabarangpur', 'Nabarangpur'),
                    ('Nayagarh', 'Nayagarh'), ('Nuapada', 'Nuapada'), ('Puri', 'Puri'), ('Rayagada', 'Rayagada'),
                    ('Sambalpur', 'Sambalpur'), ('Sonepur', 'Sonepur'), ('Sundargarh', 'Sundargarh'),
                    ('Karaikal', 'Karaikal'),
                    ('Mahe', 'Mahe'), ('Pondicherry', 'Pondicherry'), ('Yanam', 'Yanam'), ('Amritsar', 'Amritsar'),
                    ('Barnala', 'Barnala'), ('Bathinda', 'Bathinda'), ('Faridkot', 'Faridkot'),
                    ('Fatehgarh Sahib', 'Fatehgarh Sahib'),
                    ('Fazilka', 'Fazilka'), ('Ferozepur', 'Ferozepur'), ('Gurdaspur', 'Gurdaspur'),
                    ('Hoshiarpur', 'Hoshiarpur'),
                    ('Jalandhar', 'Jalandhar'), ('Kapurthala', 'Kapurthala'), ('Ludhiana', 'Ludhiana'),
                    ('Mansa', 'Mansa'),
                    ('Moga', 'Moga'), ('Muktsar', 'Muktsar'),
                    ('Nawanshahr (Shahid Bhagat Singh Nagar)', 'Nawanshahr (Shahid Bhagat Singh Nagar)'),
                    ('Pathankot', 'Pathankot'),
                    ('Patiala', 'Patiala'), ('Rupnagar', 'Rupnagar'),
                    ('Sahibzada Ajit Singh Nagar (Mohali)', 'Sahibzada Ajit Singh Nagar (Mohali)'),
                    ('Sangrur', 'Sangrur'),
                    ('Tarn Taran', 'Tarn Taran'), ('Ajmer', 'Ajmer'), ('Alwar', 'Alwar'), ('Banswara', 'Banswara'),
                    ('Baran', 'Baran'),
                    ('Barmer', 'Barmer'), ('Bharatpur', 'Bharatpur'), ('Bhilwara', 'Bhilwara'), ('Bikaner', 'Bikaner'),
                    ('Bundi', 'Bundi'), ('Chittorgarh', 'Chittorgarh'), ('Churu', 'Churu'), ('Dausa', 'Dausa'),
                    ('Dholpur', 'Dholpur'),
                    ('Dungarpur', 'Dungarpur'), ('Hanumangarh', 'Hanumangarh'), ('Jaipur', 'Jaipur'),
                    ('Jaisalmer', 'Jaisalmer'),
                    ('Jalore', 'Jalore'), ('Jhalawar', 'Jhalawar'), ('Jhunjhunu', 'Jhunjhunu'), ('Jodhpur', 'Jodhpur'),
                    ('Karauli', 'Karauli'), ('Kota', 'Kota'), ('Nagaur', 'Nagaur'), ('Pali', 'Pali'),
                    ('Pratapgarh', 'Pratapgarh'),
                    ('Rajsamand', 'Rajsamand'), ('Sawai Madhopur', 'Sawai Madhopur'), ('Sikar', 'Sikar'),
                    ('Sirohi', 'Sirohi'),
                    ('Sri Ganganagar', 'Sri Ganganagar'), ('Tonk', 'Tonk'), ('Udaipur', 'Udaipur'),
                    ('East Sikkim', 'East Sikkim'),
                    ('North Sikkim', 'North Sikkim'), ('South Sikkim', 'South Sikkim'), ('West Sikkim', 'West Sikkim'),
                    ('Ariyalur', 'Ariyalur'), ('Chennai', 'Chennai'), ('Coimbatore', 'Coimbatore'),
                    ('Cuddalore', 'Cuddalore'),
                    ('Dharmapuri', 'Dharmapuri'), ('Dindigul', 'Dindigul'), ('Erode', 'Erode'),
                    ('Kanchipuram', 'Kanchipuram'),
                    ('Kanyakumari', 'Kanyakumari'), ('Karur', 'Karur'), ('Krishnagiri', 'Krishnagiri'),
                    ('Madurai', 'Madurai'),
                    ('Nagapattinam', 'Nagapattinam'), ('Namakkal', 'Namakkal'), ('Nilgiris', 'Nilgiris'),
                    ('Perambalur', 'Perambalur'),
                    ('Pudukkottai', 'Pudukkottai'), ('Ramanathapuram', 'Ramanathapuram'), ('Salem', 'Salem'),
                    ('Sivaganga', 'Sivaganga'), ('Thanjavur', 'Thanjavur'), ('Theni', 'Theni'),
                    ('Thoothukudi (Tuticorin)', 'Thoothukudi (Tuticorin)'), ('Tiruchirappalli', 'Tiruchirappalli'),
                    ('Tirunelveli', 'Tirunelveli'), ('Tiruppur', 'Tiruppur'), ('Tiruvallur', 'Tiruvallur'),
                    ('Tiruvannamalai', 'Tiruvannamalai'), ('Tiruvarur', 'Tiruvarur'), ('Vellore', 'Vellore'),
                    ('Viluppuram', 'Viluppuram'), ('Virudhunagar', 'Virudhunagar'), ('Adilabad', 'Adilabad'),
                    ('Bhadradri Kothagudem', 'Bhadradri Kothagudem'), ('Hyderabad', 'Hyderabad'),
                    ('Jagtial', 'Jagtial'),
                    ('Jangaon', 'Jangaon'), ('Jayashankar Bhoopalpally', 'Jayashankar Bhoopalpally'),
                    ('Jogulamba Gadwal', 'Jogulamba Gadwal'), ('Kamareddy', 'Kamareddy'), ('Karimnagar', 'Karimnagar'),
                    ('Khammam', 'Khammam'), ('Komaram Bheem Asifabad', 'Komaram Bheem Asifabad'),
                    ('Mahabubabad', 'Mahabubabad'),
                    ('Mahabubnagar', 'Mahabubnagar'), ('Mancherial', 'Mancherial'), ('Medak', 'Medak'),
                    ('Medchal', 'Medchal'),
                    ('Nagarkurnool', 'Nagarkurnool'), ('Nalgonda', 'Nalgonda'), ('Nirmal', 'Nirmal'),
                    ('Nizamabad', 'Nizamabad'),
                    ('Peddapalli', 'Peddapalli'), ('Rajanna Sircilla', 'Rajanna Sircilla'),
                    ('Rangareddy', 'Rangareddy'),
                    ('Sangareddy', 'Sangareddy'), ('Siddipet', 'Siddipet'), ('Suryapet', 'Suryapet'),
                    ('Vikarabad', 'Vikarabad'),
                    ('Wanaparthy', 'Wanaparthy'), ('Warangal (Rural)', 'Warangal (Rural)'),
                    ('Warangal (Urban)', 'Warangal (Urban)'),
                    ('Yadadri Bhuvanagiri', 'Yadadri Bhuvanagiri'), ('Dhalai', 'Dhalai'), ('Gomati', 'Gomati'),
                    ('Khowai', 'Khowai'),
                    ('North Tripura', 'North Tripura'), ('Sepahijala', 'Sepahijala'),
                    ('South Tripura', 'South Tripura'),
                    ('Unakoti', 'Unakoti'), ('West Tripura', 'West Tripura'), ('Almora', 'Almora'),
                    ('Bageshwar', 'Bageshwar'),
                    ('Chamoli', 'Chamoli'), ('Champawat', 'Champawat'), ('Dehradun', 'Dehradun'),
                    ('Haridwar', 'Haridwar'),
                    ('Nainital', 'Nainital'), ('Pauri Garhwal', 'Pauri Garhwal'), ('Pithoragarh', 'Pithoragarh'),
                    ('Rudraprayag', 'Rudraprayag'), ('Tehri Garhwal', 'Tehri Garhwal'),
                    ('Udham Singh Nagar', 'Udham Singh Nagar'),
                    ('Uttarkashi', 'Uttarkashi'), ('Agra', 'Agra'), ('Aligarh', 'Aligarh'), ('Allahabad', 'Allahabad'),
                    ('Ambedkar Nagar', 'Ambedkar Nagar'),
                    ('Amethi (Chatrapati Sahuji Mahraj Nagar)', 'Amethi (Chatrapati Sahuji Mahraj Nagar)'),
                    ('Amroha (J.P. Nagar)', 'Amroha (J.P. Nagar)'), ('Auraiya', 'Auraiya'), ('Azamgarh', 'Azamgarh'),
                    ('Baghpat', 'Baghpat'), ('Bahraich', 'Bahraich'), ('Ballia', 'Ballia'), ('Balrampur', 'Balrampur'),
                    ('Banda', 'Banda'), ('Barabanki', 'Barabanki'), ('Bareilly', 'Bareilly'), ('Basti', 'Basti'),
                    ('Bhadohi', 'Bhadohi'), ('Bijnor', 'Bijnor'), ('Budaun', 'Budaun'), ('Bulandshahr', 'Bulandshahr'),
                    ('Chandauli', 'Chandauli'), ('Chitrakoot', 'Chitrakoot'), ('Deoria', 'Deoria'), ('Etah', 'Etah'),
                    ('Etawah', 'Etawah'), ('Faizabad', 'Faizabad'), ('Farrukhabad', 'Farrukhabad'),
                    ('Fatehpur', 'Fatehpur'),
                    ('Firozabad', 'Firozabad'), ('Gautam Buddha Nagar', 'Gautam Buddha Nagar'),
                    ('Ghaziabad', 'Ghaziabad'),
                    ('Ghazipur', 'Ghazipur'), ('Gonda', 'Gonda'), ('Gorakhpur', 'Gorakhpur'), ('Hamirpur', 'Hamirpur'),
                    ('Hapur (Panchsheel Nagar)', 'Hapur (Panchsheel Nagar)'), ('Hardoi', 'Hardoi'),
                    ('Hathras', 'Hathras'),
                    ('Jalaun', 'Jalaun'), ('Jaunpur', 'Jaunpur'), ('Jhansi', 'Jhansi'), ('Kannauj', 'Kannauj'),
                    ('Kanpur Dehat', 'Kanpur Dehat'), ('Kanpur Nagar', 'Kanpur Nagar'),
                    ('Kanshiram Nagar (Kasganj)', 'Kanshiram Nagar (Kasganj)'), ('Kaushambi', 'Kaushambi'),
                    ('Kushinagar (Padrauna)', 'Kushinagar (Padrauna)'), ('Lakhimpur - Kheri', 'Lakhimpur - Kheri'),
                    ('Lalitpur', 'Lalitpur'), ('Lucknow', 'Lucknow'), ('Maharajganj', 'Maharajganj'),
                    ('Mahoba', 'Mahoba'),
                    ('Mainpuri', 'Mainpuri'), ('Mathura', 'Mathura'), ('Mau', 'Mau'), ('Meerut', 'Meerut'),
                    ('Mirzapur', 'Mirzapur'),
                    ('Moradabad', 'Moradabad'), ('Muzaffarnagar', 'Muzaffarnagar'), ('Pilibhit', 'Pilibhit'),
                    ('Pratapgarh', 'Pratapgarh'), ('RaeBareli', 'RaeBareli'), ('Rampur', 'Rampur'),
                    ('Saharanpur', 'Saharanpur'),
                    ('Sambhal (Bhim Nagar)', 'Sambhal (Bhim Nagar)'), ('Sant Kabir Nagar', 'Sant Kabir Nagar'),
                    ('Shahjahanpur', 'Shahjahanpur'), ('Shamali (Prabuddh Nagar)', 'Shamali (Prabuddh Nagar)'),
                    ('Shravasti', 'Shravasti'), ('Siddharth Nagar', 'Siddharth Nagar'), ('Sitapur', 'Sitapur'),
                    ('Sonbhadra', 'Sonbhadra'), ('Sultanpur', 'Sultanpur'), ('Unnao', 'Unnao'),
                    ('Varanasi', 'Varanasi'),
                    ('Alipurduar', 'Alipurduar'), ('Bankura', 'Bankura'), ('Birbhum', 'Birbhum'),
                    ('Burdwan (Bardhaman)', 'Burdwan (Bardhaman)'), ('Cooch Behar', 'Cooch Behar'),
                    ('Dakshin Dinajpur (South Dinajpur)', 'Dakshin Dinajpur (South Dinajpur)'),
                    ('Darjeeling', 'Darjeeling'),
                    ('Hooghly', 'Hooghly'), ('Howrah', 'Howrah'), ('Jalpaiguri', 'Jalpaiguri'),
                    ('Kalimpong', 'Kalimpong'),
                    ('Kolkata', 'Kolkata'), ('Malda', 'Malda'), ('Murshidabad', 'Murshidabad'), ('Nadia', 'Nadia'),
                    ('North 24 Parganas', 'North 24 Parganas'),
                    ('Paschim Medinipur (West Medinipur)', 'Paschim Medinipur (West Medinipur)'),
                    ('Purba Medinipur (East Medinipur)', 'Purba Medinipur (East Medinipur)'), ('Purulia', 'Purulia'),
                    ('South 24 Parganas', 'South 24 Parganas'),
                    ('Uttar Dinajpur (North Dinajpur)', 'Uttar Dinajpur (North Dinajpur)')]

gender_select = ((None, "Gender"),
                 ("Male", "Male"),
                 ("Female", "Female"),
                 ("Female", "Other"))
category_select = ((None, 'Reservations'),
                   ("SC", "SC"),
                   ("ST", "ST"),
                   ("OEC", "OEC"),
                   ("OBC", "OBC"),
                   ("GEN", "GEN"))

department_select = [(None, "Select Department")]
print ("Departments")
for i in Department.objects.all():
    department_select.append((i.Department , i.Department))
print (department_select)
# department_select = [(None, "Select Department"), ('DDU Kaushal Kendras (DDUKK)', 'DDU Kaushal Kendras (DDUKK)'),
#                      ('Department of Applied Chemistry', 'Department of Applied Chemistry'),
#                      ('Department of Applied Economics', 'Department of Applied Economics'),
#                      ('Department of Atmospheric Sciences', 'Department of Atmospheric Sciences'),
#                      ('Department of Biotechnology', 'Department of Biotechnology'),
#                      ('Department of Chemical Oceanography', 'Department of Chemical Oceanography'),
#                      ('Department of Computer Applications', 'Department of Computer Applications'),
#                      ('Department of Computer Science', 'Department of Computer Science'),
#                      ('Department of Electronics', 'Department of Electronics'),
#                      ('Department of Hindi', 'Department of Hindi'),
#                      ('Department of Instrumentation', 'Department of Instrumentation'), (
#                          'Department of Marine Biology, Microbiology and Biochemistry',
#                          'Department of Marine Biology, Microbiology and Biochemistry'),
#                      ('Department of Marine Geology and Geophysics', 'Department of Marine Geology and Geophysics'),
#                      ('Department of Mathematics', 'Department of Mathematics'),
#                      ('Department of Physical Oceanography', 'Department of Physical Oceanography'),
#                      ('Department of Physics', 'Department of Physics'), (
#                          'Department of Polymer Science and Rubber Technology',
#                          'Department of Polymer Science and Rubber Technology'),
#                      ('Department of Ship Technology', 'Department of Ship Technology'),
#                      ('Department of Statistics', 'Department of Statistics'), (
#                          'Inter University Centre for IPR Studies (IUCIPRS)',
#                          'Inter University Centre for IPR Studies (IUCIPRS)'),
#                      ('International School of Photonics', 'International School of Photonics'), (
#                          'National Centre for Aquatic Animal Health (NCAAH)',
#                          'National Centre for Aquatic Animal Health (NCAAH)'),
#                      ('School of Engineering', 'School of Engineering'),
#                      ('School of Environmental Studies', 'School of Environmental Studies'),
#                      ('School of Industrial Fisheries', 'School of Industrial Fisheries'),
#                      ('School of Legal Studies', 'School of Legal Studies'),
#                      ('School of Management Studies', 'School of Management Studies')]

course_select = [(None, 'Select Course'), ('M.Voc', 'M.Voc'), ('B.Voc', 'B.Voc'), ('M.Sc', 'M.Sc'),
                 ('Integrated M.Sc', 'Integrated M.Sc'),
                 ('M.Phil', 'M.Phil'), ('Ph.D', 'Ph.D'), ('M.A', 'M.A'), ('M.Tech', 'M.Tech'), ('MCA', 'MCA'),
                 ('MSc', 'MSc'), ('B.Tech', 'B.Tech'), ('LLM', 'LLM'), ('Civil Engg.(B.Tech)', 'Civil Engg.(B.Tech)'),
                 ('Computer Science & Engg.(B.Tech)', 'Computer Science & Engg.(B.Tech)'),
                 ('Electrical and Electronics Engg.(B.Tech)', 'Electrical and Electronics Engg.(B.Tech)'),
                 ('Electronics & Communication Engg.(B.Tech)', 'Electronics & Communication Engg.(B.Tech)'),
                 ('Information Technology(B.Tech)', 'Information Technology(B.Tech)'),
                 ('Mechanical Engg.(B.Tech)', 'Mechanical Engg.(B.Tech)'),
                 ('Safety & Fire Engg(B.Tech)', 'Safety & Fire Engg(B.Tech)'),
                 ('Civil Engg.(M.Tech)', 'Civil Engg.(M.Tech)'),
                 ('Computer Science & Engg.(M.Tech)', 'Computer Science & Engg.(M.Tech)'),
                 ('Electrical and Electronics Engg.(M.Tech)', 'Electrical and Electronics Engg.(M.Tech)'),
                 ('Electronics & Communication Engg.(M.Tech)', 'Electronics & Communication Engg.(M.Tech)'),
                 ('Information Technology(M.Tech)', 'Information Technology(M.Tech)'),
                 ('Mechanical Engg.(M.Tech)', 'Mechanical Engg.(M.Tech)'),
                 ('Safety & Fire Engg(M.Tech)', 'Safety & Fire Engg(M.Tech)'), ('LLB', 'LLB'), ('MBA', 'MBA')]

year_select = (
    (None, 'year for which allotment is required',),
    (5, "5th Year"),
    (4, "4th Year",),
    (3, "3rd Year",),
    (2, "2nd Year",),
    (1, "1st Year",),

)

sub_category_choices = (
    (None, "Select Sub Category"),
    ("OBH", "OBH"),
    ("OBX (LC,Anglo India)", "OBX (LC,Anglo Indian"),
    ("MS (Muslim)", "MS (Muslim)")
)

hostel_select = (
    (None, "Select"),
)


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


def user_directory_path(instance, filename):
    extension = os.path.splitext(filename)[1].lower()

    return 'user_{0}{1}'.format(instance.user.id, extension)


class Applications(models.Model):
    user = models.OneToOneField(login_models.VerifiedUser, on_delete=models.CASCADE)
    Registration_No = TextField(max_length=255)
    Name = TextField(max_length=255)
    Address_For_Communication = TextField(max_length=512)
    Permanent_Address = TextField(max_length=512)
    Pincode = IntegerField(default=0, blank=False)
    State = CharField(max_length=255, choices=state_choices, default=0, blank=False)
    District = TextField(max_length=255, choices=district_choices, default=0, blank=False)
    Mobile_Number = CharField(max_length=255, default=0, blank=False)
    Name_of_Guardian = TextField(max_length=255)
    PhoneNumber_of_Guardian = CharField(max_length=255, default=0, blank=False)
    Year_of_Study = IntegerField(choices=year_select, default=0, blank=False)
    Gender = CharField(max_length=255, choices=gender_select, default=0, blank=False)
    Category = CharField(max_length=255, choices=category_select, default=0, blank=False)
    Sub_Category = CharField(max_length=255, choices=sub_category_choices, default=None, blank=True, null=True)
    Physically_Handicapped = IntegerField(default=0)
    Keralite = IntegerField(default=0)
    Department = CharField(max_length=255, choices=department_select, default=0, blank=False)
    Course_of_study = CharField(max_length=255, choices=course_select, default=0, blank=False)
    Admission_date = DateField(default=timezone.now)
    Course_completion_date = DateField(default=timezone.now)
    CAT_Rank = IntegerField(default=0, null=True, blank=True)
    Prime_Ministers_program = IntegerField(default=0)
    Photo_upload = models.FileField(upload_to=user_directory_path,
                                    storage=OverwriteStorage(location=settings.MEDIA_ROOT),
                                    default='settings.MEDIA_ROOT/anonymous.jpg')
    isvalid = models.BooleanField(default=1, blank=True, null=True)
    category_isvalid = models.BooleanField(default=1, blank=True, null=True)
    distance = models.IntegerField(default=25, blank=True, null=True)
    attendance = models.BooleanField(default=1, blank=True, null=True)
    year_back = models.BooleanField(default=0, blank=True, null=True)
    admitted = models.BooleanField(default=0, blank=True, null=True)
    verified_department = models.BooleanField(default=0, blank=True, null=True)
    Hostel_admitted = CharField(max_length=255, choices=hostel_select, default=None, blank=True, null=True)
    Room_No = CharField(max_length=255, default=0)
    Date_of_application = models.DateField(null=True,blank=True)
    Date_of_birth = models.DateField(default=timezone.now())

    def create_priority_value(self):
        priority_value = self.distance
        if self.Keralite == 1:
            if self.Category == 'SC' or self.Category == 'ST':
                if (self.category_isvalid == 1):
                    priority_value += 100000000
                else:
                    priority_value += 0
            if self.Category == 'OEC':
                if (self.category_isvalid == 1):
                    priority_value += 5000000
                else:
                    priority_value += 0
        if self.Prime_Ministers_program or self.State == "Lakshadweep (UT)":
            priority_value += 10000000
        if self.Physically_Handicapped:
            priority_value += 1000000
        priority_value += self.Year_of_Study * 10000
        return priority_value

    def distance_valid(self):
        if (
                self.Category == 'SC' or self.Category == 'ST' or self.Category == 'OEC' or self.Physically_Handicapped == 1):
            return True
        else:
            if (self.distance < 25):
                return False
            else:
                return True


@receiver(post_save, sender=login_models.VerifiedUser)
def create_user_application(sender, instance, created, **kwargs):
    if created:
        Applications.objects.create(user=instance)


@receiver(post_save, sender=login_models.VerifiedUser)
def save_user_application(sender, instance, **kwargs):
    instance.applications.save()
