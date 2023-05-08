# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
import dataclasses
from typing import Any, Dict, Optional, List, Iterator, TypedDict

from google.generativeai.types import safety_types
from google.generativeai.types import citation_types


__all__ = ["Completion"]


class TextCompletion(TypedDict, total=False):
    output: str
    safety_ratings: Optional[List[safety_types.SafetyRatingDict]]
    citation_metadata: Optional[citation_types.CitationMetadataDict]


@dataclasses.dataclass(init=False)
class Completion(abc.ABC):
    """The result returned by `generativeai.generate_text`.

    Use `GenerateTextResponse.candidates` to access all the completions generated by the model.

    Attributes:
        candidates: A list of candidate text completions generated by the model.
        result: The output of the first candidate,
        filters: Indicates the reasons why content may have been blocked
          Either Unspecified, Safety, or Other. See `types.ContentFilter`.
        safety_feedback: Indicates which safety settings blocked content in this result.
    """

    candidates: List[TextCompletion]
    result: Optional[str]
    filters: Optional[list[safety_types.ContentFilterDict]]
    safety_feedback: Optional[list[safety_types.SafetyFeedbackDict]]

    def to_dict(self) -> Dict[str, Any]:
        result = {
            "candidates": self.candidates,
            "filters": self.filters,
            "safety_feedback": self.safety_feedback,
        }
        return result
