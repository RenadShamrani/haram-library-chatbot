# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


def get_language(tracker: Tracker) -> Text:
    """Helper function to detect user language."""
    last_msg = tracker.latest_message.get('text', '').lower()
    arabic_letters = set("ابتثجحخدذرزسشصضطظعغفقكلمنهويءئؤةى")
    arabic_ratio = sum(1 for c in last_msg if c in arabic_letters) / (len(last_msg) + 1e-5)
    return "ar" if arabic_ratio > 0.5 else "en"


def localized_response(ar_text: Text, en_text: Text, tracker: Tracker) -> Text:
    """Return the appropriate response based on detected language."""
    return ar_text if get_language(tracker) == "ar" else en_text


# الردود العامة
class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = localized_response(
            "وعليكم السلام ورحمة الله وبركاته، أهلًا وسهلًا بك في مكتبة الحرم المكي الشريف. كيف يمكنني مساعدتك؟",
            "Peace be upon you. Welcome to the Grand Mosque Library. How can I assist you?",
            tracker)
        dispatcher.utter_message(text=text)
        return []


class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = localized_response(
            "شكرًا لتواصلك معنا. نتمنى لك يومًا سعيدًا. في أمان الله.",
            "Thank you for contacting us. We wish you a pleasant day. Goodbye.",
            tracker)
        dispatcher.utter_message(text=text)
        return []


class ActionWelcome(Action):
    def name(self) -> Text:
        return "action_welcome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = localized_response(
            "مرحبًا بك في مساعد مكتبة الحرم المكي الشريف. أنا هنا للإجابة على استفساراتك حول خدمات ومصادر المكتبة.",
            "Welcome to the Grand Mosque Library Assistant. I'm here to answer your questions about the library's services and resources.",
            tracker)
        dispatcher.utter_message(text=text)
        return []


class ActionFarewell(Action):
    def name(self) -> Text:
        return "action_farewell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = localized_response(
            "إذا احتجت لأي مساعدة مستقبلًا، لا تتردد في العودة. دمت بخير.",
            "If you need any help in the future, feel free to return. Take care.",
            tracker)
        dispatcher.utter_message(text=text)
        return []

# الأكشنات المخصصة لكل FAQ

faq_mapping = {
    "action_faq_hours": (
        "تعمل المكتبة من الأحد إلى الخميس، من الساعة 8:00 صباحًا حتى 8:00 مساءً.",
        "The library operates from Sunday to Thursday, from 8:00 AM to 8:00 PM."
    ),
    "action_faq_location": (
        "تقع مكتبة الحرم المكي الشريف في حي بطحاء قريش، بجوار جامع الإمام أحمد بن حنبل.",
        "The Grand Mosque Library is located in Batha Quraysh District, next to Imam Ahmad bin Hanbal Mosque."
    ),
    "action_faq_services": (
        "توفر المكتبة مجموعة متنوعة من الخدمات مثل الاطلاع الداخلي، الفهرس الإلكتروني، المخطوطات، قواعد البيانات، والمساعدة المرجعية.",
        "The library offers various services including internal reading, electronic catalog, manuscripts, databases, and reference assistance."
    ),
    "action_faq_manuscripts": (
        "نعم، تتوفر نسخ مصوّرة من المخطوطات حفاظًا عليها، وهي متاحة للباحثين والباحثات للاطلاع والدراسة.",
        "Yes, digitized copies of manuscripts are available for preservation purposes, and can be accessed by researchers for study."
    ),
    "action_faq_rules": (
        "الدخول للمكتبة متاح للجميع، مع الالتزام بالهدوء، والحفاظ على الكتب، وعدم استخدام الهاتف في القاعات.",
        "Entry to the library is open to all, provided that visitors maintain silence, preserve books, and avoid using phones in the halls."
    ),
    "action_faq_help": (
        "يسرنا مساعدتك! تفضل بطرح سؤالك أو استفسارك وسنقوم بتوجيهك حسب الحاجة.",
        "We are happy to assist you! Please go ahead and ask your question, and we’ll guide you accordingly."
    ),
    "action_faq_rooms": (
        "نعم، توفر المكتبة غرفًا وقاعات يمكن استخدامها حسب السياسات المعتمدة من الإدارة.",
        "Yes, the library provides rooms and halls that can be used according to the approved policies."
    ),
    "action_faq_events": (
        "نعم، تُنظم المكتبة العديد من الفعاليات والأنشطة العلمية والثقافية، حضورياً أو افتراضياً.",
        "Yes, the library organizes various academic and cultural events, both in-person and virtual."
    ),
    "action_faq_internet": (
        "نعم، توجد خدمة إنترنت وأجهزة حاسوب داخل المكتبة لاستخدامها في البحث والاطلاع.",
        "Yes, internet service and computers are available in the library for research and browsing."
    ),
    "action_faq_borrow": (
        "حاليًا، خدمة الإعارة غير متوفّرة في المكتبة.",
        "Currently, the borrowing service is not available at the library."
    ),
    "action_faq_buy_books": (
        "المصادر المتاحة في المكتبة مخصصة للاطلاع والاستفادة منها فقط، ولا تُعرض للبيع.",
        "The materials available in the library are for reference use only and are not for sale."
    ),
    "action_faq_novels": (
        "نعم، تشمل مجموعات المكتبة مجموعة واسعة من الكتب تغطي معظم مجالات المعرفة، بما في ذلك القصص والروايات.",
        "Yes, the library's collections include a wide range of books covering most fields of knowledge, including stories and novels."
    ),
    "action_faq_ebooks": (
        "حاليًا، المتاح هو كتب ورقية، ويوجد في المستودع الرقمي على موقع المكتبة بعض الكتب النادرة متاحة بصيغة إلكترونية بالكامل.",
        "Currently, only printed books are available. However, some rare books are fully available in digital format on the library's website."
    ),
    "action_faq_copy_policy": (
        "يُسمح بتصوير ما لا يتجاوز 25٪ من محتوى الكتاب، مراعاةً لحقوق الملكية الفكرية للمؤلف.",
        "Up to 25% of a book's content can be copied in compliance with the author's intellectual property rights."
    ),
    "action_faq_suggestions": (
        "يسرنا استقبال اقتراحاتكم لإثراء مجموعات المكتبة. يمكنك طلب إضافة كتاب عبر القنوات الرسمية للمكتبة.",
        "We welcome your suggestions to enrich the library’s collections. You may request book additions via the official library channels."
    ),
    "action_faq_classification_code": (
        "يُستخدم رمز التصنيف لتحديد موضوع الكتاب، وهو يعتمد على نظام ديوي العشري العالمي.",
        "The classification code is used to determine the book’s subject and follows the Dewey Decimal Classification system."
    ),
    "action_faq_help_subject": (
        "بالتأكيد، فريق خدمات المستفيدين موجود دائمًا لمساعدتك في الوصول إلى المواد المناسبة لموضوعك.",
        "Certainly, the user services team is always available to help you find resources relevant to your topic."
    ),
    "action_faq_help_databases": (
        "نعم، يوجد فريق مختص بالإضافة إلى مواد تعليمية مرئية لمساعدتك في استخدام قواعد البيانات.",
        "Yes, a specialized team and visual learning materials are available to help you use the databases."
    ),
    "action_faq_search_book": (
        "يمكنك البحث من خلال الفهرس الآلي المتاح على موقع المكتبة الرسمي حسب العنوان، المؤلف، أو الموضوع.",
        "You can search via the library’s online catalog by title, author, or subject."
    ),
    "action_faq_documents_required": (
        "مكتبة الحرم المكي الشريف مكتبة عامة، وخدماتها متاحة لكافة أفراد المجتمع دون الحاجة إلى مستندات خاصة.",
        "The Grand Mosque Library is a public library, and its services are available to all members of the community without the need for specific documents."
    ),
    "action_faq_rare_books": (
        "نعم، تحتوي المكتبة على قسم مخصّص للكتب النادرة، وتُعامل تلك الكتب بعناية خاصة للحفاظ عليها.",
        "Yes, the library has a special section for rare books, which are handled with special care for preservation."
    ),
    "action_faq_printing": (
        "حاليًا، يتوفر تصوير أوعية المعلومات الخاصة بالمكتبة لخدمة الباحثين وطلبة العلم فقط.",
        "Currently, reproduction of the library's information materials is available only to researchers and students of knowledge."
    ),
    "action_faq_meeting_rooms": (
        "نعم، يُمكن استخدام القاعات حسب السياسات المعتمدة من إدارة المكتبة، ويرجى التنسيق المسبق.",
        "Yes, halls can be used according to the library's policies, and prior coordination is required."
    ),
    "action_faq_suggest_book": (
        "نعم، يُمكنك اقتراح إضافة كتاب، وسيتم دراسة الطلب ضمن خطط التزويد المعتمدة.",
        "Yes, you may suggest a book addition, and the request will be considered within the approved acquisition plans."
    ),
    "action_faq_book_location": (
        "يمكن تحديد مكان الكتاب باستخدام رقم التصنيف ورقم الوعاء الموجود على البطاقة الخاصة به.",
        "The book's location can be identified using the classification number and the container number listed on its card."
    ),
    "action_faq_anything_else": (
        "هل هناك أمر آخر يمكنني مساعدتك فيه؟",
        "Is there anything else I can assist you with?"
    ),
}


# توليد الكلاسات تلقائيًا لجميع الأكشنات في القاموس
for action_name, (ar, en) in faq_mapping.items():
    exec(f"""
class {action_name.title().replace('_', '')}(Action):
    def name(self) -> Text:
        return "{action_name}"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = localized_response({repr(ar)}, {repr(en)}, tracker)
        dispatcher.utter_message(text=text)
        return []
""")