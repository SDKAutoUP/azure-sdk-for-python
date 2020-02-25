# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
from azure.core.exceptions import HttpResponseError, ClientAuthenticationError
import platform
from azure.core.exceptions import HttpResponseError
from azure.ai.textanalytics import (
    VERSION,
    TextAnalyticsClient,
    DetectLanguageInput,
    TextDocumentInput,
    TextAnalyticsApiKeyCredential
)
from testcase import TextAnalyticsTest, GlobalTextAnalyticsAccountPreparer


class TestBatchTextAnalytics(TextAnalyticsTest):

    @pytest.mark.live_test_only
    def test_active_directory_auth(self):
        token = self.generate_oauth_token()
        endpoint = self.get_oauth_endpoint()
        text_analytics = TextAnalyticsClient(endpoint, token)

        docs = [{"id": "1", "text": "I should take my cat to the veterinarian."},
                {"id": "2", "text": "Este es un document escrito en Español."},
                {"id": "3", "text": "猫は幸せ"},
                {"id": "4", "text": "Fahrt nach Stuttgart und dann zum Hotel zu Fu."}]

        response = text_analytics.detect_language(docs)

    @GlobalTextAnalyticsAccountPreparer()
    def test_empty_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        with self.assertRaises(TypeError):
            text_analytics = TextAnalyticsClient(text_analytics_account, "")

    @GlobalTextAnalyticsAccountPreparer()
    def test_bad_type_for_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        with self.assertRaises(TypeError):
            text_analytics = TextAnalyticsClient(text_analytics_account, [])

    @GlobalTextAnalyticsAccountPreparer()
    def test_none_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        with self.assertRaises(ValueError):
            text_analytics = TextAnalyticsClient(text_analytics_account, None)

    @GlobalTextAnalyticsAccountPreparer()
    def test_bad_input_to_method(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        with self.assertRaises(TypeError):
            response = text_analytics.detect_language("hello world")

    @GlobalTextAnalyticsAccountPreparer()
    def test_successful_detect_language(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "text": "I should take my cat to the veterinarian."},
                {"id": "2", "text": "Este es un document escrito en Español."},
                {"id": "3", "text": "猫は幸せ"},
                {"id": "4", "text": "Fahrt nach Stuttgart und dann zum Hotel zu Fu."}]

        response = text_analytics.detect_language(docs, show_stats=True)

        self.assertEqual(response[0].primary_language.name, "English")
        self.assertEqual(response[1].primary_language.name, "Spanish")
        self.assertEqual(response[2].primary_language.name, "Japanese")
        self.assertEqual(response[3].primary_language.name, "German")
        self.assertEqual(response[0].primary_language.iso6391_name, "en")
        self.assertEqual(response[1].primary_language.iso6391_name, "es")
        self.assertEqual(response[2].primary_language.iso6391_name, "ja")
        self.assertEqual(response[3].primary_language.iso6391_name, "de")

        for doc in response:
            self.assertIsNotNone(doc.id)
            self.assertIsNotNone(doc.statistics)
            self.assertIsNotNone(doc.primary_language.score)

    @GlobalTextAnalyticsAccountPreparer()
    def test_some_errors_detect_language(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "country_hint": "United States", "text": "I should take my cat to the veterinarian."},
                {"id": "2", "text": "Este es un document escrito en Español."},
                {"id": "3", "text": ""},
                {"id": "4", "text": "Fahrt nach Stuttgart und dann zum Hotel zu Fu."}]

        response = text_analytics.detect_language(docs)

        self.assertTrue(response[0].is_error)
        self.assertFalse(response[1].is_error)
        self.assertTrue(response[2].is_error)
        self.assertFalse(response[3].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_all_errors_detect_language(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        text = ""
        for _ in range(5121):
            text += "x"

        docs = [{"id": "1", "text": ""},
                {"id": "2", "text": ""},
                {"id": "3", "text": ""},
                {"id": "4", "text": text}]

        response = text_analytics.detect_language(docs)

        for resp in response:
            self.assertTrue(resp.is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_language_detection_empty_credential_class(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(""))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.detect_language(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_language_detection_bad_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential("xxxxxxxxxxxx"))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.detect_language(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_language_detection_bad_model_version(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        with self.assertRaises(HttpResponseError):
            response = text_analytics.detect_language(
                inputs=["Microsoft was founded by Bill Gates."],
                model_version="old"
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_successful_recognize_entities(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "en", "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975."},
                {"id": "2", "language": "es", "text": "Microsoft fue fundado por Bill Gates y Paul Allen el 4 de abril de 1975."},
                {"id": "3", "language": "de", "text": "Microsoft wurde am 4. April 1975 von Bill Gates und Paul Allen gegründet."}]

        response = text_analytics.recognize_entities(docs, show_stats=True)
        for doc in response:
            self.assertEqual(len(doc.entities), 4)
            self.assertIsNotNone(doc.id)
            self.assertIsNotNone(doc.statistics)
            for entity in doc.entities:
                self.assertIsNotNone(entity.text)
                self.assertIsNotNone(entity.category)
                self.assertIsNotNone(entity.offset)
                self.assertIsNotNone(entity.length)
                self.assertIsNotNone(entity.score)

    @GlobalTextAnalyticsAccountPreparer()
    def test_some_errors_recognize_entities(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "en", "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975."},
                {"id": "2", "language": "Spanish", "text": "Hola"},
                {"id": "3", "language": "de", "text": ""}]

        response = text_analytics.recognize_entities(docs)
        self.assertFalse(response[0].is_error)
        self.assertTrue(response[1].is_error)
        self.assertTrue(response[2].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_all_errors_recognize_entities(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "text": ""},
                {"id": "2", "language": "Spanish", "text": "Hola"},
                {"id": "3", "language": "de", "text": ""}]

        response = text_analytics.recognize_entities(docs)
        self.assertTrue(response[0].is_error)
        self.assertTrue(response[1].is_error)
        self.assertTrue(response[2].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_entity_recognition_empty_credential_class(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(""))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.recognize_entities(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_entity_recognition_bad_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential("xxxxxxxxxxxx"))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.recognize_entities(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_entity_recognition_bad_model_version(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        with self.assertRaises(HttpResponseError):
            response = text_analytics.recognize_entities(
                inputs=["Microsoft was founded by Bill Gates."],
                model_version="old"
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_successful_recognize_pii_entities(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "text": "My SSN is 555-55-5555."},
                {"id": "2", "text": "Your ABA number - 111000025 - is the first 9 digits in the lower left hand corner of your personal check."},
                {"id": "3", "text": "Is 998.214.865-68 your Brazilian CPF number?"}]

        response = text_analytics.recognize_pii_entities(docs, show_stats=True)
        self.assertEqual(response[0].entities[0].text, "555-55-5555")
        self.assertEqual(response[0].entities[0].category, "U.S. Social Security Number (SSN)")
        self.assertEqual(response[1].entities[0].text, "111000025")
        # self.assertEqual(response[1].entities[0].category, "ABA Routing Number")  # Service is currently returning PhoneNumber here
        self.assertEqual(response[2].entities[0].text, "998.214.865-68")
        self.assertEqual(response[2].entities[0].category, "Brazil CPF Number")
        for doc in response:
            self.assertIsNotNone(doc.id)
            self.assertIsNotNone(doc.statistics)
            for entity in doc.entities:
                self.assertIsNotNone(entity.text)
                self.assertIsNotNone(entity.category)
                self.assertIsNotNone(entity.offset)
                self.assertIsNotNone(entity.length)
                self.assertIsNotNone(entity.score)

    @GlobalTextAnalyticsAccountPreparer()
    def test_some_errors_recognize_pii_entities(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "es", "text": "hola"},
                {"id": "2", "text": ""},
                {"id": "3", "text": "Is 998.214.865-68 your Brazilian CPF number?"}]

        response = text_analytics.recognize_pii_entities(docs)
        self.assertTrue(response[0].is_error)
        self.assertTrue(response[1].is_error)
        self.assertFalse(response[2].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_all_errors_recognize_pii_entities(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "es", "text": "hola"},
                {"id": "2", "text": ""}]

        response = text_analytics.recognize_pii_entities(docs)
        self.assertTrue(response[0].is_error)
        self.assertTrue(response[1].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_pii_entity_recognition_empty_credential_class(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(""))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.recognize_pii_entities(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_pii_entity_recognition_bad_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential("xxxxxxxxxxxx"))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.recognize_pii_entities(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_pii_entity_recognition_bad_model_version(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        with self.assertRaises(HttpResponseError):
            response = text_analytics.recognize_pii_entities(
                inputs=["Microsoft was founded by Bill Gates."],
                model_version="old"
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_successful_recognize_linked_entities(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "en", "text": "Microsoft was founded by Bill Gates and Paul Allen"},
                {"id": "2", "language": "es", "text": "Microsoft fue fundado por Bill Gates y Paul Allen"}]

        response = text_analytics.recognize_linked_entities(docs, show_stats=True)
        for doc in response:
            self.assertEqual(len(doc.entities), 3)
            self.assertIsNotNone(doc.id)
            self.assertIsNotNone(doc.statistics)
            for entity in doc.entities:
                self.assertIsNotNone(entity.name)
                self.assertIsNotNone(entity.matches)
                self.assertIsNotNone(entity.language)
                self.assertIsNotNone(entity.data_source_entity_id)
                self.assertIsNotNone(entity.url)
                self.assertIsNotNone(entity.data_source)

    @GlobalTextAnalyticsAccountPreparer()
    def test_some_errors_recognize_linked_entities(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "text": ""},
                {"id": "2", "language": "es", "text": "Microsoft fue fundado por Bill Gates y Paul Allen"}]

        response = text_analytics.recognize_linked_entities(docs)
        self.assertTrue(response[0].is_error)
        self.assertFalse(response[1].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_all_errors_recognize_linked_entities(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "text": ""},
                {"id": "2", "language": "Spanish", "text": "Microsoft fue fundado por Bill Gates y Paul Allen"}]

        response = text_analytics.recognize_linked_entities(docs)
        self.assertTrue(response[0].is_error)
        self.assertTrue(response[1].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_linked_entity_recognition_empty_credential_class(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(""))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.recognize_linked_entities(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_linked_entity_recognition_bad_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential("xxxxxxxxxxxx"))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.recognize_linked_entities(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_linked_entity_recognition_bad_model_version(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        with self.assertRaises(HttpResponseError):
            response = text_analytics.recognize_linked_entities(
                inputs=["Microsoft was founded by Bill Gates."],
                model_version="old"
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_successful_extract_key_phrases(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "en", "text": "Microsoft was founded by Bill Gates and Paul Allen"},
                {"id": "2", "language": "es", "text": "Microsoft fue fundado por Bill Gates y Paul Allen"}]

        response = text_analytics.extract_key_phrases(docs, show_stats=True)
        for phrases in response:
            self.assertIn("Paul Allen", phrases.key_phrases)
            self.assertIn("Bill Gates", phrases.key_phrases)
            self.assertIn("Microsoft", phrases.key_phrases)
            self.assertIsNotNone(phrases.id)
            self.assertIsNotNone(phrases.statistics)

    @GlobalTextAnalyticsAccountPreparer()
    def test_some_errors_extract_key_phrases(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "English", "text": "Microsoft was founded by Bill Gates and Paul Allen"},
                {"id": "2", "language": "es", "text": "Microsoft fue fundado por Bill Gates y Paul Allen"}]

        response = text_analytics.extract_key_phrases(docs)
        self.assertTrue(response[0].is_error)
        self.assertFalse(response[1].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_all_errors_extract_key_phrases(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "English", "text": "Microsoft was founded by Bill Gates and Paul Allen"},
                {"id": "2", "language": "es", "text": ""}]

        response = text_analytics.extract_key_phrases(docs)
        self.assertTrue(response[0].is_error)
        self.assertTrue(response[1].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_key_phrases_empty_credential_class(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(""))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.extract_key_phrases(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_key_phrases_bad_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential("xxxxxxxxxxxx"))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.extract_key_phrases(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_key_phrases_bad_model_version(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        with self.assertRaises(HttpResponseError):
            response = text_analytics.extract_key_phrases(
                inputs=["Microsoft was founded by Bill Gates."],
                model_version="old"
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_successful_analyze_sentiment(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "en", "text": "Microsoft was founded by Bill Gates and Paul Allen."},
                {"id": "2", "language": "en", "text": "I did not like the hotel we stayed it. It was too expensive."},
                {"id": "3", "language": "en", "text": "The restaurant had really good food. I recommend you try it."}]

        response = text_analytics.analyze_sentiment(docs, show_stats=True)
        self.assertEqual(response[0].sentiment, "neutral")
        self.assertEqual(response[1].sentiment, "negative")
        self.assertEqual(response[2].sentiment, "positive")
        for doc in response:
            self.assertIsNotNone(doc.id)
            self.assertIsNotNone(doc.statistics)
            self.assertIsNotNone(doc.confidence_scores)
            self.assertIsNotNone(doc.sentences)

    @GlobalTextAnalyticsAccountPreparer()
    def test_some_errors_analyze_sentiment(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "en", "text": ""},
                {"id": "2", "language": "english", "text": "I did not like the hotel we stayed it. It was too expensive."},
                {"id": "3", "language": "en", "text": "The restaurant had really good food. I recommend you try it."}]

        response = text_analytics.analyze_sentiment(docs)
        self.assertTrue(response[0].is_error)
        self.assertTrue(response[1].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_all_errors_analyze_sentiment(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "en", "text": ""},
                {"id": "2", "language": "english", "text": "I did not like the hotel we stayed it. It was too expensive."},
                {"id": "3", "language": "en", "text": ""}]

        response = text_analytics.analyze_sentiment(docs)
        self.assertTrue(response[0].is_error)
        self.assertTrue(response[1].is_error)
        self.assertTrue(response[2].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_analyze_sentiment_empty_credential_class(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(""))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.analyze_sentiment(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_analyze_sentiment_bad_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential("xxxxxxxxxxxx"))
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.analyze_sentiment(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_analyze_sentiment_bad_model_version(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        with self.assertRaises(HttpResponseError):
            response = text_analytics.analyze_sentiment(
                inputs=["Microsoft was founded by Bill Gates."],
                model_version="old"
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_validate_input_string(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [
            u"I should take my cat to the veterinarian.",
            u"Este es un document escrito en Español.",
            u"猫は幸せ",
            u"Fahrt nach Stuttgart und dann zum Hotel zu Fu.",
            u""
        ]

        response = text_analytics.detect_language(docs)
        self.assertEqual(response[0].primary_language.name, "English")
        self.assertEqual(response[1].primary_language.name, "Spanish")
        self.assertEqual(response[2].primary_language.name, "Japanese")
        self.assertEqual(response[3].primary_language.name, "German")
        self.assertTrue(response[4].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    def test_validate_language_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [
            DetectLanguageInput(id="1", text="I should take my cat to the veterinarian."),
            DetectLanguageInput(id="2", text="Este es un document escrito en Español."),
            DetectLanguageInput(id="3", text="猫は幸せ"),
            DetectLanguageInput(id="4", text="Fahrt nach Stuttgart und dann zum Hotel zu Fu.")
        ]

        response = text_analytics.detect_language(docs)
        self.assertEqual(response[0].primary_language.name, "English")
        self.assertEqual(response[1].primary_language.name, "Spanish")
        self.assertEqual(response[2].primary_language.name, "Japanese")
        self.assertEqual(response[3].primary_language.name, "German")

    @GlobalTextAnalyticsAccountPreparer()
    def test_validate_multilanguage_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [
            TextDocumentInput(id="1", text="Microsoft was founded by Bill Gates and Paul Allen."),
            TextDocumentInput(id="2", text="I did not like the hotel we stayed it. It was too expensive."),
            TextDocumentInput(id="3", text="The restaurant had really good food. I recommend you try it."),
        ]

        response = text_analytics.analyze_sentiment(docs)
        self.assertEqual(response[0].sentiment, "neutral")
        self.assertEqual(response[1].sentiment, "negative")
        self.assertEqual(response[2].sentiment, "positive")

    @GlobalTextAnalyticsAccountPreparer()
    def test_mixing_inputs(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        docs = [
            {"id": "1", "text": "Microsoft was founded by Bill Gates and Paul Allen."},
            TextDocumentInput(id="2", text="I did not like the hotel we stayed it. It was too expensive."),
            u"You cannot mix string input with the above inputs"
        ]
        with self.assertRaises(TypeError):
            response = text_analytics.analyze_sentiment(docs)

    @GlobalTextAnalyticsAccountPreparer()
    def test_out_of_order_ids(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "56", "text": ":)"},
                {"id": "0", "text": ":("},
                {"id": "22", "text": ""},
                {"id": "19", "text": ":P"},
                {"id": "1", "text": ":D"}]

        response = text_analytics.analyze_sentiment(docs)
        in_order = ["56", "0", "22", "19", "1"]
        for idx, resp in enumerate(response):
            self.assertEqual(resp.id, in_order[idx])

    @GlobalTextAnalyticsAccountPreparer()
    def test_show_stats_and_model_version(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(response):
            self.assertIsNotNone(response.model_version)
            self.assertIsNotNone(response.raw_response)
            self.assertEqual(response.statistics.document_count, 5)
            self.assertEqual(response.statistics.transaction_count, 4)
            self.assertEqual(response.statistics.valid_document_count, 4)
            self.assertEqual(response.statistics.erroneous_document_count, 1)

        docs = [{"id": "56", "text": ":)"},
                {"id": "0", "text": ":("},
                {"id": "22", "text": ""},
                {"id": "19", "text": ":P"},
                {"id": "1", "text": ":D"}]

        response = text_analytics.analyze_sentiment(
            docs,
            show_stats=True,
            model_version="latest",
            response_hook=callback
        )

    @GlobalTextAnalyticsAccountPreparer()
    def test_batch_size_over_limit(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [u"hello world"] * 1050
        with self.assertRaises(HttpResponseError):
            response = text_analytics.detect_language(docs)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_country_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            country_str = "\"countryHint\": \"CA\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 3)

        docs = [
            u"This was the best day of my life.",
            u"I did not like the hotel we stayed it. It was too expensive.",
            u"The restaurant was not as good as I hoped."
        ]

        response = text_analytics.detect_language(docs, country_hint="CA", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_dont_use_country_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            country_str = "\"countryHint\": \"\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 3)

        docs = [
            u"This was the best day of my life.",
            u"I did not like the hotel we stayed it. It was too expensive.",
            u"The restaurant was not as good as I hoped."
        ]

        response = text_analytics.detect_language(docs, country_hint="", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_per_item_dont_use_country_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            country_str = "\"countryHint\": \"\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 2)
            country_str = "\"countryHint\": \"US\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 1)


        docs = [{"id": "1", "country_hint": "", "text": "I will go to the park."},
                {"id": "2", "country_hint": "", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.detect_language(docs, response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_country_hint_and_obj_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            country_str = "\"countryHint\": \"CA\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 3)

        docs = [
            DetectLanguageInput(id="1", text="I should take my cat to the veterinarian."),
            DetectLanguageInput(id="2", text="Este es un document escrito en Español."),
            DetectLanguageInput(id="3", text="猫は幸せ"),
        ]

        response = text_analytics.detect_language(docs, country_hint="CA", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_country_hint_and_dict_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            country_str = "\"countryHint\": \"CA\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 3)

        docs = [{"id": "1", "text": "I will go to the park."},
                {"id": "2", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.detect_language(docs, country_hint="CA", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_country_hint_and_obj_per_item_hints(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            country_str = "\"countryHint\": \"CA\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 2)
            country_str = "\"countryHint\": \"US\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 1)

        docs = [
            DetectLanguageInput(id="1", text="I should take my cat to the veterinarian.", country_hint="CA"),
            DetectLanguageInput(id="4", text="Este es un document escrito en Español.", country_hint="CA"),
            DetectLanguageInput(id="3", text="猫は幸せ"),
        ]

        response = text_analytics.detect_language(docs, country_hint="US", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_country_hint_and_dict_per_item_hints(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            country_str = "\"countryHint\": \"CA\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 1)
            country_str = "\"countryHint\": \"US\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 2)

        docs = [{"id": "1", "country_hint": "US", "text": "I will go to the park."},
                {"id": "2", "country_hint": "US", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.detect_language(docs, country_hint="CA", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_language_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"fr\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        docs = [
            u"This was the best day of my life.",
            u"I did not like the hotel we stayed it. It was too expensive.",
            u"The restaurant was not as good as I hoped."
        ]

        response = text_analytics.analyze_sentiment(docs, language="fr", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_dont_use_language_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        docs = [
            u"This was the best day of my life.",
            u"I did not like the hotel we stayed it. It was too expensive.",
            u"The restaurant was not as good as I hoped."
        ]

        response = text_analytics.analyze_sentiment(docs, language="", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_per_item_dont_use_language_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 2)
            language_str = "\"language\": \"en\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 1)


        docs = [{"id": "1", "language": "", "text": "I will go to the park."},
                {"id": "2", "language": "", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.analyze_sentiment(docs, response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_language_hint_and_obj_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"de\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        docs = [
            TextDocumentInput(id="1", text="I should take my cat to the veterinarian."),
            TextDocumentInput(id="4", text="Este es un document escrito en Español."),
            TextDocumentInput(id="3", text="猫は幸せ"),
        ]

        response = text_analytics.analyze_sentiment(docs, language="de", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_language_hint_and_dict_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"es\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        docs = [{"id": "1", "text": "I will go to the park."},
                {"id": "2", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.analyze_sentiment(docs, language="es", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_language_hint_and_obj_per_item_hints(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"es\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 2)
            language_str = "\"language\": \"en\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 1)

        docs = [
            TextDocumentInput(id="1", text="I should take my cat to the veterinarian.", language="es"),
            TextDocumentInput(id="2", text="Este es un document escrito en Español.", language="es"),
            TextDocumentInput(id="3", text="猫は幸せ"),
        ]

        response = text_analytics.analyze_sentiment(docs, language="en", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_whole_batch_language_hint_and_dict_per_item_hints(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"es\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 2)
            language_str = "\"language\": \"en\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 1)


        docs = [{"id": "1", "language": "es", "text": "I will go to the park."},
                {"id": "2", "language": "es", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.analyze_sentiment(docs, language="en", response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_bad_document_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = "This is the wrong type"

        with self.assertRaises(TypeError):
            response = text_analytics.analyze_sentiment(docs)

    @GlobalTextAnalyticsAccountPreparer()
    def test_client_passed_default_country_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key), default_country_hint="CA")

        def callback(resp):
            country_str = "\"countryHint\": \"CA\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 3)

        def callback_2(resp):
            country_str = "\"countryHint\": \"DE\""
            country = resp.http_request.body.count(country_str)
            self.assertEqual(country, 3)

        docs = [{"id": "1", "text": "I will go to the park."},
                {"id": "2", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.detect_language(docs, response_hook=callback)
        response = text_analytics.detect_language(docs, country_hint="DE", response_hook=callback_2)
        response = text_analytics.detect_language(docs, response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_client_passed_default_language_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key), default_language="es")

        def callback(resp):
            language_str = "\"language\": \"es\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        def callback_2(resp):
            language_str = "\"language\": \"en\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        docs = [{"id": "1", "text": "I will go to the park."},
                {"id": "2", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.analyze_sentiment(docs, response_hook=callback)
        response = text_analytics.analyze_sentiment(docs, language="en", response_hook=callback_2)
        response = text_analytics.analyze_sentiment(docs, response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_rotate_subscription_key(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        credential = TextAnalyticsApiKeyCredential(text_analytics_account_key)
        text_analytics = TextAnalyticsClient(text_analytics_account, credential)

        docs = [{"id": "1", "text": "I will go to the park."},
                {"id": "2", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.analyze_sentiment(docs)
        self.assertIsNotNone(response)

        credential.update_key("xxx")  # Make authentication fail
        with self.assertRaises(ClientAuthenticationError):
            response = text_analytics.analyze_sentiment(docs)

        credential.update_key(text_analytics_account_key)  # Authenticate successfully again
        response = text_analytics.analyze_sentiment(docs)
        self.assertIsNotNone(response)

    @GlobalTextAnalyticsAccountPreparer()
    def test_user_agent(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            self.assertIn("azsdk-python-azure-ai-textanalytics/{} Python/{} ({})".format(
                VERSION, platform.python_version(), platform.platform()),
                resp.http_request.headers["User-Agent"]
            )

        docs = [{"id": "1", "text": "I will go to the park."},
                {"id": "2", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = text_analytics.analyze_sentiment(docs, response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_document_attribute_error(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "text": ""}]
        response = text_analytics.analyze_sentiment(docs)

        # Attributes on DocumentError
        self.assertTrue(response[0].is_error)
        self.assertEqual(response[0].id, "1")
        self.assertIsNotNone(response[0].error)

        # Result attribute not on DocumentError, custom error message
        try:
            sentiment = response[0].sentiment
        except AttributeError as custom_error:
            self.assertEqual(
                custom_error.args[0],
                '\'DocumentError\' object has no attribute \'sentiment\'. '
                'The service was unable to process this document:\nDocument Id: 1\nError: '
                'invalidDocument - Document text is empty.\n'
            )

        # Attribute not found on DocumentError or result obj, default behavior/message
        try:
            sentiment = response[0].attribute_not_on_result_or_error
        except AttributeError as default_behavior:
            self.assertEqual(
                default_behavior.args[0],
                '\'DocumentError\' object has no attribute \'attribute_not_on_result_or_error\''
            )

    @GlobalTextAnalyticsAccountPreparer()
    def test_text_analytics_error(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        text = ""
        for _ in range(5121):
            text += "x"

        docs = [{"id": "1", "text": ""},
                {"id": "2", "language": "english", "text": "I did not like the hotel we stayed it."},
                {"id": "3", "text": text}]

        # Bad model version
        try:
            result = text_analytics.analyze_sentiment(docs, model_version="bad")
        except HttpResponseError as err:
            self.assertEqual(err.error_code, "InvalidRequest")
            self.assertIsNotNone(err.message)

        # DocumentErrors
        doc_errors = text_analytics.analyze_sentiment(docs)
        self.assertEqual(doc_errors[0].error.code, "invalidDocument")
        self.assertIsNotNone(doc_errors[0].error.message)
        self.assertEqual(doc_errors[1].error.code, "unsupportedLanguageCode")
        self.assertIsNotNone(doc_errors[1].error.message)
        self.assertEqual(doc_errors[2].error.code, "invalidDocument")
        self.assertIsNotNone(doc_errors[2].error.message)

        # Missing input records
        docs = []
        try:
            result = text_analytics.analyze_sentiment(docs)
        except HttpResponseError as err:
            self.assertEqual(err.error_code, "MissingInputRecords")
            self.assertIsNotNone(err.message)

        # Duplicate Ids
        docs = [{"id": "1", "text": "hello world"},
                {"id": "1", "text": "I did not like the hotel we stayed it."}]
        try:
            result = text_analytics.analyze_sentiment(docs)
        except HttpResponseError as err:
            self.assertEqual(err.error_code, "InvalidDocument")
            self.assertIsNotNone(err.message)

        # Batch size over limit
        docs = [u"hello world"] * 1001
        try:
            response = text_analytics.detect_language(docs)
        except HttpResponseError as err:
            self.assertEqual(err.error_code, "InvalidDocumentBatch")
            self.assertIsNotNone(err.message)

        # Service bug returns invalidDocument here. Uncomment after v3.0-preview.2
        # docs = [{"id": "1", "country_hint": "United States", "text": "hello world"}]
        #
        # response = text_analytics.detect_language(docs)
        # self.assertEqual(response[0].error.code, "invalidCountryHint")
        # self.assertIsNotNone(response[0].error.message)

    @GlobalTextAnalyticsAccountPreparer()
    def test_text_analytics_country_hint_none(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        # service will eventually support this and we will not need to send "" for input == "none"
        documents = [{"id": "0", "country_hint": "none", "text": "This is written in English."}]
        documents2 = [DetectLanguageInput(id="1", country_hint="none", text="This is written in English.")]

        def callback(response):
            country_str = "\"countryHint\": \"\""
            country = response.http_request.body.count(country_str)
            self.assertEqual(country, 1)

        # test dict
        result = text_analytics.detect_language(documents, response_hook=callback)
        # test DetectLanguageInput
        result2 = text_analytics.detect_language(documents2, response_hook=callback)
        # test per-operation
        result3 = text_analytics.detect_language(inputs=["this is written in english"], country_hint="none", response_hook=callback)
        # test client default
        new_client = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key), default_country_hint="none")
        result4 = new_client.detect_language(inputs=["this is written in english"], response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    def test_keyword_arguments(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(response):
            country_str = "\"countryHint\": \"ES\""
            self.assertEqual(response.http_request.body.count(country_str), 1)
            self.assertIsNotNone(response.model_version)
            self.assertIsNotNone(response.statistics)

        def callback2(response):
            language_str = "\"language\": \"es\""
            self.assertEqual(response.http_request.body.count(language_str), 1)
            self.assertIsNotNone(response.model_version)
            self.assertIsNotNone(response.statistics)

        def callback3(response):
            language_str = "\"language\": \"en\""
            self.assertEqual(response.http_request.body.count(language_str), 1)
            self.assertIsNotNone(response.model_version)
            self.assertIsNotNone(response.statistics)

        res = text_analytics.detect_language(
            inputs=["this is written in english"],
            model_version="latest",
            show_stats=True,
            country_hint="ES",
            response_hook=callback
        )

        res = text_analytics.recognize_entities(
            inputs=["Bill Gates is the CEO of Microsoft."],
            model_version="latest",
            show_stats=True,
            language="es",
            response_hook=callback2
        )

        res = text_analytics.recognize_linked_entities(
            inputs=["Bill Gates is the CEO of Microsoft."],
            model_version="latest",
            show_stats=True,
            language="es",
            response_hook=callback2
        )

        res = text_analytics.recognize_pii_entities(
            inputs=["Bill Gates is the CEO of Microsoft."],
            model_version="latest",
            show_stats=True,
            language="en",
            response_hook=callback3
        )

        res = text_analytics.analyze_sentiment(
            inputs=["Bill Gates is the CEO of Microsoft."],
            model_version="latest",
            show_stats=True,
            language="es",
            response_hook=callback2
        )