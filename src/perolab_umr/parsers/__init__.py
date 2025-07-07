from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from perolab_umr.parsers.parser import NewParser

        return NewParser(**self.model_dump())


class perolabExperimentParserEntryPoint(ParserEntryPoint):

    def load(self):
        from perolab_umr.parsers.perolab_batch_parser import perolabExperimentParser

        return perolabExperimentParser(**self.model_dump())


class perolabParserEntryPoint(ParserEntryPoint):

    def load(self):
        from perolab_umr.parsers.perolab_measurement_parser import perolabParser

        return perolabParser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


perolab_experiment_parser_entry_point = perolabExperimentParserEntryPoint(
    name='perolabExperimentParserEntryPoint',
    description='perolab experiment parser entry point configuration.',
    mainfile_name_re='^(.+\.xlsx)$',
    mainfile_mime_re='(application|text|image)/.*',
)


perolab_parser_entry_point = perolabParserEntryPoint(
    name='perolabParserEntryPoint',
    description='perolab parser entry point configuration.',
    mainfile_name_re='^.+\.?.+\.((eqe|jv|mppt)\..{1,4})$',
    mainfile_mime_re='(application|text|image)/.*',
)
